from numpy import zeros
from random import randint

class EstruturasDados:

    def __init__(self):
        pass

    def gerar_matriz(self):
        qtd_cidades = int(input("Quantidade de cidades da rota: "))
        self.matriz = zeros((qtd_cidades, qtd_cidades), dtype=int)
        for i in self.matriz:
            for g in self.matriz:
                if i!=g:
                    self.matriz[i][g] = randint(1, 10)
        self.exibir_dados()
    
    def exibir_dados(self):
        print(self.matriz)

ed = EstruturasDados()
ed.gerar_matriz()

#gerar matriz.