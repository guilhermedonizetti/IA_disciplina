from numpy import zeros

class EstruturasDados:

    def __init__(self):
        #As cidades representam os nos (pontos do grafo)
        self.cidades = ["Queluz", "Cruzeiro", "Cachoeira P.", "Piquete", "Lorena"]
        #As ligacoes são as arestas de um ponto aos pontos possiveis
        #O indice da lista de ligacoes corresponde a cidade que esta no mesmo indice na lista de cidades
        self.ligacoes = [
            ["Cruzeiro"],
            ["Queluz", "Cachoeira P.", "Piquete"],
            ["Cruzeiro", "Piquete", "Lorena"],
            ["Cruzeiro", "Cachoeira P."],
            ["Cachoeira P."]
        ]

    def gerar_matriz(self):
        """Transforma as listas de cidades e ligacoes em matriz de adjacencias.
        \nPara cada Cidade, ele deixa 0 se nao houver ligacao.
        \nDeixa 1 se existir ligacao."""
        qtd_cidades = len(self.cidades)
        self.matriz = zeros((qtd_cidades, qtd_cidades), dtype=int)
        for i in range(len(self.matriz)):
            nos = self.nos_cidades(i)
            for g in range(len(self.matriz)):
                if g in nos:
                    self.matriz[i][g] = 1
        self.exibir_dados()
    
    def nos_cidades(self, indice):
        """Cria uma lista com os nos que fazem ligacao com a cidade do indice passado."""
        nos = []
        for i in self.ligacoes[indice]:
            nos.append(self.cidades.index(i))
        return nos
    
    def exibir_dados(self):
        print(self.matriz)

ed = EstruturasDados()
ed.gerar_matriz()