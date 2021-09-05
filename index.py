import streamlit as st
import pydeck as pdk
from datetime import datetime
from agente import Agente
from lista_cidades import lista_cidades
from coordenadas import coordenadas

class RotasCidades:

    def __init__(self):
        self.cidades = lista_cidades
        self.cidade_final = ""
        self.horario = datetime.now()

    #metodo que ira iniciar quando a pagina carregar
    def inicial(self):
        """Inicia a pagina com esses elementos"""

        st.set_page_config(page_title="Rotas Cidades")
        st.title("Rotas Cidades")
        texto = "Cidade para receber Ajuda Humanitária:"
        self.cidade_final = st.sidebar.selectbox(texto, self.cidades)
        buscar_rota = st.sidebar.checkbox("Buscar rota")

        if buscar_rota:
            self.gerar_rota()
    
    #metodo para gerar a rota de Ajuda Humanitaria e Atendimento
    def gerar_rota(self):
        agente = Agente()
        rota_AH = agente.profundidade(self.cidade_final)
        rota_At = agente.encontrar_atendimento(self.cidade_final)
        rota_final = agente.unifica_caminho(rota_AH, rota_At)
        st.json(rota_final)
        self.busca_coordenadas(rota_final)
    
    #metodo para fazer as coordenadas
    def busca_coordenadas(self, rota):
        coord = coordenadas
        coord_da_rota = []
        for i in rota:
            posicao = self.cidades.index(i)
            coord_da_rota.append(coord[posicao])
        
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
        st.json(coord_rota)
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
                "Outbound Flow": pdk.Layer(
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
                estilo = self.HoraEstilo()
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
    
    def HoraEstilo(self):
        hora = str(self.horario)
        hora = hora.split(" ")
        hora = hora[1].split(":")
        if int(hora[0])>6 and int(hora[0])<18:
            return "mapbox://styles/mapbox/streets-v11"
        else:
            return "mapbox://styles/mapbox/dark-v10"

if __name__ == "__main__":
    rc = RotasCidades()
    rc.inicial()