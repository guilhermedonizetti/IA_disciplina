import streamlit as st
import pydeck as pdk
from requests import get
from json import loads
from datetime import datetime
from agente import Agente
from lista_cidades import lista_cidades

class RotasCidades:

    def __init__(self):
        self.limite = False
        self.cidades = lista_cidades
        self.cidade_final = ""
        self.metodos_opcoes = ["AMPLITUDE", "PROFUNDIDADE", "PROFUNDIDADE LIMITADA",
                               "APROFUNDAMENTO ITERATIVO", "BIDIRECIONAL"]

    #metodo que ira iniciar quando a pagina carregar
    def inicial(self):
        """Inicia a pagina com esses elementos"""

        st.set_page_config(page_title="Rotas Cidades")
        st.title("Rotas Cidades")
        texto1 = "Cidade para receber Ajuda Humanitária:"
        self.cidade_final = st.sidebar.selectbox(texto1, self.cidades)
        texto2 = "Método para gerar a rota:"
        self.metodo = st.sidebar.selectbox(texto2, self.metodos_opcoes)
        if self.metodo == self.metodos_opcoes[2]:
            buscar_rota = False
            texto = "Informe o limite da rota:"
            self.limite = st.sidebar.number_input(texto, min_value=1, step=1, max_value=10)
        buscar_rota = st.sidebar.checkbox("Buscar rota")

        if buscar_rota:
            self.gerar_rota()
    
    #metodo para gerar a rota de Ajuda Humanitaria e Atendimento
    def gerar_rota(self):
        agente = Agente()
        rota_AH = agente.encontrar_ajuda_humanitaria(self.cidade_final, self.metodo, self.limite)
        rota_AT = agente.encontrar_atendimento(self.cidade_final, self.metodo, self.limite)
        #rota_AH = agente.profundidade(self.cidade_final)
        #rota_AH = agente.busca_profundidade_limitada(self.cidade_final)
        #rota_At = agente.encontrar_atendimento(self.cidade_final)
        rota_final = agente.unifica_caminho(rota_AH, rota_AT)
        
        st.info("Ajuda Humanitária sai de: {}.".format(rota_final[0]))
        st.info("O Atendimento mais próximo é: {}.".format(rota_final[len(rota_final)-1]))
        if len(rota_final)>=3:
            desc = self.descrever_rota(rota_final)
            st.success(desc)
        self.busca_coordenadas(rota_final)
    
    #metodo para fazer as coordenadas
    def busca_coordenadas(self, rota):
        coord_da_rota = []
        for i in rota:
            requisicao = get("https://api-valeparaiba.herokuapp.com/valedoparaiba/coordenadas/{}/".format(i))
            lat_lon = loads(requisicao.content)
            coord_da_rota.append(lat_lon)
        
        for i in range(len(coord_da_rota)):
            if i == len(coord_da_rota)-1:
                coord_da_rota[i]['lat2'] = coord_da_rota[i]['lat']
                coord_da_rota[i]['lon2'] = coord_da_rota[i]['lon']
            else:
                coord_da_rota[i]['lat2'] = coord_da_rota[i+1]['lat']
                coord_da_rota[i]['lon2'] = coord_da_rota[i+1]['lon']
        
        self.plotar_mapa(coord_da_rota)
    
    #metodo para desenhar e exibir mapa
    def plotar_mapa(self, coord_rota):
        try:
            ALL_LAYERS = {
                "Pontos": pdk.Layer(
                    "ScatterplotLayer",
                    data=coord_rota,
                    get_position=["lon", "lat"],
                    get_color=[210, 50, 192, 50],
                    get_radius=30000,
                    radius_scale=0.05,
                ),
                "Ligações": pdk.Layer(
                    "ArcLayer",
                    data=coord_rota,
                    get_source_position=["lon", "lat"],
                    get_target_position=["lon2", "lat2"],
                    get_source_color=[200, 30, 0, 160],
                    get_target_color=[200, 30, 0, 160],
                    auto_highlight=True,
                    width_scale=0.1,
                    get_width="outbound",
                    width_min_pixels=3,
                    width_max_pixels=30,
                )
            }
            st.sidebar.markdown('### Opções')
            selected_layers = [
                layer for layer_name, layer in ALL_LAYERS.items()
                if st.sidebar.checkbox(layer_name, True)
            ]
            if selected_layers:
                estilo = "mapbox://styles/mapbox/streets-v11"
                st.pydeck_chart(pdk.Deck(
                    map_style=estilo,
                    initial_view_state={"latitude": coord_rota[0]["lat"], #37.76
                                        "longitude": coord_rota[0]["lon"], "pitch": 50},
                    layers=selected_layers,
                ))
            else:
                st.error("Please choose at least one layer above.")
        except:
            st.error("Algum erro aconteceu.")
    
    #Funcao para descrever a rota
    def descrever_rota(self, rota):
        desc = "Saindo de {}, você deverá passar por ".format(rota[0])
        for i in range(1, len(rota)):
            if i == len(rota)-1:
                desc = desc+" e por fim {}.".format(rota[i])
            else:
                desc = desc+" {},".format(rota[i])
        return desc

if __name__ == "__main__":
    rc = RotasCidades()
    rc.inicial()