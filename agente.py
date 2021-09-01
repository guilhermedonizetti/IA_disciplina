"""Este modulo se refere ao agente:
\naquele que chama os metodos conforme o necessario."""

from main import Busca

class Agente(Busca):

    def __init__(self):
        self.pontos_ajuda_hum = ["CRUZEIRO", "GUARATINGUETÁ",
                    "SÃO SEBASTIÃO", "TAUBATÉ", "CAÇAPAVA"]

        self.pontos_atendimento = ["SÃO JOSÉ DOS CAMPOS", "LORENAS",
                    "UBATUBA", "QUELUZ", "TREMEMBÉ"]

    def encontrar_caminho(self):
        """Metodo para encontrar um caminho entre dois pontos."""
        cidade_final = input("Ajuda Humanitária para (cidade): ")

        tam_caminho = 10000
        for i in self.pontos_ajuda_hum:
            caminho = self.caminho(i, cidade_final.upper())
            if len(caminho) < tam_caminho:
                tam_caminho = len(caminho)
                rota = caminho

        print("\nA rota mais curta é: {}".format(rota))
        self.encontrar_atendimento(cidade_final)

    def encontrar_atendimento(self, cidade_inicial):
        tam_caminho = 10000
        for i in self.pontos_atendimento:
            caminho = self.caminho(cidade_inicial.upper(), i)
            if len(caminho) < tam_caminho:
                tam_caminho = len(caminho)
                rota = caminho

        print("\nO caminho para o atendimento é: {}".format(rota))

agente = Agente()
agente.encontrar_caminho()