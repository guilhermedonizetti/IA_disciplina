"""Este modulo se refere ao agente:
\naquele que chama os metodos conforme o necessario."""

from main import Busca

class Agente(Busca):

    def __init__(self):
        pass

    def encontrar_caminho(self):
        """Metodo para encontrar um caminho entre dois pontos."""
        cidade_inicial = input("Cidade inicial: ")
        cidade_final = input("Cidade final: ")
        caminho = self.caminho(cidade_inicial, cidade_final)

        print(caminho)

agente = Agente()
agente.encontrar_caminho()