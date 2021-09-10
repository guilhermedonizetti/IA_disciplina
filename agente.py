"""Este modulo se refere ao agente:
\naquele que chama os metodos conforme o necessario."""

from main import Busca
from time import time

class Agente(Busca):

    #Inicializa as listas que sao de valores padrao
    def __init__(self):
        #Define 5 cidades para pontos de Ajuda Humanitaria
        self.pontos_ajuda_hum = ["CRUZEIRO", "GUARATINGUETÁ",
                    "TAUBATÉ", "SÃO JOSÉ DOS CAMPOS", "CARAGUATATUBA"]

        #Define 10 cidades para ponto de Atendimento hospitalar
        self.pontos_atendimento = ["QUELUZ", "CRUZEIRO", "LORENA",
                    "GUARANTINGUETÁ", "APARECIDA", "TAUBATÉ",
                    "PINDAMONHANGABA", "SÃO JOSÉ DOS CAMPOS",
                    "CAÇAPAVA", "SÃO SEBASTIÃO"]
        
        self.rota_Ajuda_Hum =  self.rota_atendimento = []

    def encontrar_atendimento(self, cidade_final):
        """Metodo para encontrar um caminho entre a cidade que recebeu a AH e o hospi mais proximo.
        Recebe a cidade que teve a ajuda humanitaria e realiza as tentativas de gerar
        uma rota partindo dessa cidade ate a mais proxima dentre as da lista 'pontos_atendimento'."""

        tam_caminho = 100000
        for i in self.pontos_atendimento: #para cada cidade da lista tenta uma rota...
            caminho = self.caminho(cidade_final.upper(), i)
            #a menor rota sera a atual
            if len(caminho) < tam_caminho:
                tam_caminho = len(caminho)
                self.rota_atendimento = caminho
        
        return self.rota_atendimento

    def profundidade(self, cidade_final):
        """Metodo para encontrar um caminho entre dois pontos.
        Recebe a cidade que precisa da ajuda humanitaria e realiza as tentativas
        de gerar uma rota partindo das cidades da lista 'pontos_ajuda_hum' usando menos Memoria."""

        tam_caminho = 100000
        tempo_ini = time() #verifica o desempenho
        for i in self.pontos_ajuda_hum: #para cada cidade da lista tenta um caminho...
            caminho = self.caminho(i, cidade_final.upper())
            #o menor caminho sera o atual
            if len(caminho) < tam_caminho:
                tam_caminho = len(caminho)
                self.rota_Ajuda_Hum = caminho

        return self.rota_Ajuda_Hum
    
    def unifica_caminho(self, rota_AH, rota_At):
        """Metodo para unificar o caminho, unir as rotas de AH e Atendimento"""

        caminho_unico = []
        for i in rota_AH:
            caminho_unico.append(i)
        for g in range(1, len(rota_At)):
            caminho_unico.append(rota_At[g])
        
        return caminho_unico
