"""Este modulo se refere ao agente:
\naquele que chama os metodos conforme o necessario."""

from main import Busca
from time import time

class Agente(Busca):

    #Inicializa as listas que sao de valores padrao
    def __init__(self):
        self.pontos_ajuda_hum = ["CRUZEIRO", "GUARATINGUETÁ",
                    "SÃO SEBASTIÃO", "TAUBATÉ", "CAÇAPAVA"]

        self.pontos_atendimento = ["SÃO JOSÉ DOS CAMPOS", "LORENAS",
                    "UBATUBA", "QUELUZ", "TREMEMBÉ"]

    def encontrar_caminho(self):
        """Metodo para encontrar um caminho entre dois pontos.
        Recebe a cidade que precisa da ajuda humanitaria e realiza as tentativas
        de gerar uma rota partindo das cidades da lista 'pontos_ajuda_hum'."""

        cidade_final = input("Ajuda Humanitária para (cidade): ") #recebe a cidade que precisa de AH

        tam_caminho = 100000
        tempo_ini = time() #para verificar o desempenho
        for i in self.pontos_ajuda_hum: #a cada cidade da lista, tenta um camino...
            caminho = self.caminho(i, cidade_final.upper())
            #se o caminho for menor ele sera o atual
            if len(caminho) < tam_caminho:
                tam_caminho = len(caminho)
                rota = caminho

        print("\nA rota mais curta é: {}\nTempo: {}".format(rota, time()-tempo_ini))
        self.encontrar_atendimento(cidade_final) #Gerar um caminho para o atndimento hospitalar
        self.Profundidade(cidade_final) #Tenta outro metodo para gerar uma rota de ajuda huma.

    def encontrar_atendimento(self, cidade_inicial):
        """Metodo para encontrar um caminho entre a cidade que recebeu a AH e o hospi mais proximo.
        Recebe a cidade que teve a ajuda humanitaria e realiza as tentativas de gerar
        uma rota partindo dessa cidade ate a mais proxima dentre as da lista 'pontos_atendimento'."""

        tam_caminho = 100000
        for i in self.pontos_atendimento: #para cada cidade da lista tenta uma rota...
            caminho = self.caminho(cidade_inicial.upper(), i)
            #a menor rota sera a atual
            if len(caminho) < tam_caminho:
                tam_caminho = len(caminho)
                rota = caminho

        print("\nO caminho para o atendimento é: {}".format(rota))

    def Profundidade(self, cidade_final):
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
                rota = caminho

        print("\nProfundidade: {}\nTempo: {}".format(rota, time()-tempo_ini))

agente = Agente()
agente.encontrar_caminho()