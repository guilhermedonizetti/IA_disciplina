"""Este modulo se refere ao agente:
\no que chama os metodos conforme o necessario."""

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
        
        #Declara o nome dos metodos a serem escolhidos para comparar com a entrada
        self.metodos = ["AMPLITUDE", "PROFUNDIDADE", "PROFUNDIDADE LIMITADA",
                   "APROFUNDAMENTO ITERATIVO", "BIDIRECIONAL"]

        #Declara o nome dos metodos a serem chamados para executar
        self.metodos_main = ["amplitude", "profundidade", "profundidade_limitada",
                        "aprofundamento_iterativo", "bidirecional"]
        
        #Inicia a lista que vai receber as rotas
        self.rota_Ajuda_Hum =  self.rota_atendimento = []


    def encontrar_atendimento(self, cidade_final, metodo, limite=False):
        """Metodo para encontrar um caminho entre a cidade que recebeu a AH e o hospital mais proximo.
        Recebe a cidade que teve a ajuda humanitaria e realiza as tentativas de gerar
        uma rota partindo dessa cidade ate a mais proxima dentre as da lista 'pontos_atendimento'."""

        tam_caminho = 100000

        #se escolher Amplitude
        if metodo == self.metodos[0]:
            for i in self.pontos_atendimento: #para cada cidade da lista tenta um caminho...
                caminho = self.amplitude(cidade_final.upper(), i)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.rota_Ajuda_Hum = caminho
            return self.rota_Ajuda_Hum
        
        #se escolher Profundidade
        if metodo == self.metodos[1]:
            for i in self.pontos_atendimento: #para cada cidade da lista tenta um caminho...
                caminho = self.profundidade(cidade_final.upper(), i)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.rota_Ajuda_Hum = caminho
            return self.rota_Ajuda_Hum
        
        #se escolher Profundidade Limitada
        if metodo == self.metodos[2]:
            for i in self.pontos_atendimento: #para cada cidade da lista tenta um caminho...
                caminho = self.profundidade_limitada(cidade_final.upper(), i, 4)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.rota_Ajuda_Hum = caminho
            return self.rota_Ajuda_Hum
        
        #se escolher Aprofundamento iterativo
        if metodo == self.metodos[3]:
            for i in self.pontos_atendimento: #para cada cidade da lista tenta um caminho...
                caminho = self.aprofundamento_iterativo(cidade_final.upper(), i)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.rota_Ajuda_Hum = caminho
            return self.rota_Ajuda_Hum
        
        #se escolher Bidirecional
        if metodo == self.metodos[4]:
            for i in self.pontos_atendimento: #para cada cidade da lista tenta um caminho...
                caminho = self.bidirecional(cidade_final.upper(), i)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.rota_Ajuda_Hum = caminho
            return self.rota_Ajuda_Hum

    def encontrar_ajuda_humanitaria(self, cidade_final, metodo, limite=False):
        """Metodo para encontrar um caminho entre dois pontos.
        Recebe a cidade que precisa da ajuda humanitaria e realiza as tentativas
        de gerar uma rota partindo das cidades da lista 'pontos_ajuda_hum' usando menos Memoria."""
        
        tam_caminho = 100000

        #se escolher Amplitude
        if metodo == self.metodos[0]:
            for i in self.pontos_ajuda_hum: #para cada cidade da lista tenta um caminho...
                caminho = self.amplitude(i, cidade_final.upper())
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.rota_Ajuda_Hum = caminho
            return self.rota_Ajuda_Hum
        
        #se escolher Profundidade
        if metodo == self.metodos[1]:
            for i in self.pontos_ajuda_hum: #para cada cidade da lista tenta um caminho...
                caminho = self.profundidade(i, cidade_final.upper())
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.rota_Ajuda_Hum = caminho
            return self.rota_Ajuda_Hum
        
        #se escolher Profundidade Limitada
        if metodo == self.metodos[2]:
            for i in self.pontos_ajuda_hum: #para cada cidade da lista tenta um caminho...
                caminho = self.profundidade_limitada(i, cidade_final.upper(), 4)
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.rota_Ajuda_Hum = caminho
            return self.rota_Ajuda_Hum
        
        #se escolher Aprofundamento iterativo
        if metodo == self.metodos[3]:
            for i in self.pontos_ajuda_hum: #para cada cidade da lista tenta um caminho...
                caminho = self.aprofundamento_iterativo(i, cidade_final.upper())
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.rota_Ajuda_Hum = caminho
            return self.rota_Ajuda_Hum
        
        #se escolher Bidirecional
        if metodo == self.metodos[4]:
            for i in self.pontos_ajuda_hum: #para cada cidade da lista tenta um caminho...
                caminho = self.bidirecional(i, cidade_final.upper())
                #o menor caminho sera o atual
                if len(caminho) < tam_caminho:
                    tam_caminho = len(caminho)
                    self.rota_Ajuda_Hum = caminho
            return self.rota_Ajuda_Hum
    
    #Funcao para unir as rotas de ajuda humanitaria e atendimento
    def unifica_caminho(self, rota_AH, rota_At):
        """Metodo para unificar o caminho, unir as rotas de AH e Atendimento"""

        caminho_unico = []
        for i in rota_AH:
            caminho_unico.append(i)
        for g in range(1, len(rota_At)):
            caminho_unico.append(rota_At[g])
        
        return caminho_unico
