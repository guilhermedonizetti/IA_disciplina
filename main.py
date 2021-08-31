"""Esse modulo contem as funcoes relacionadas ao caminho"""

from lista import Lista

class Busca(Lista):

    nos = ["ARAD", "BUCARESTE", "CRAIOVA", "DOBRETA",
                    "EFORIE", "FAGARAS", "GIORGIU", "HIRSOVA",
                    "IASI", "LUGOJ", "MEHADIA", "NEAMT", "ORADEA",
                    "PITESTI", "RIMNICU VILCEA", "SIBIU", "TIMISOARA",
                    "URZICENI", "VASLUI", "ZERIND"]
    grafo = [
            ["ZERIND", "TIMISOARA", "SIBIU"],                 #indice 0
            ["URZICENI", "PITESTI", "GIORGIU", "FAGARAS"],
            ["RIMNICU VILCEA", "PITESTI", "DOBRETA"],
            ["MEHADIA", "CRAIOVA"],
            ["HIRSOVA"],
            ["SIBIU", "BUCARESTE"],
            ["BUCARESTE"],
            ["URZICENI", "EFORIE"],
            ["VASLUI", "NEAMT"],
            ["TIMISOARA", "MEHADIA"],
            ["LUGOJ", "DOBRETA"],
            ["IASI"],
            ["ZERIND", "SIBIU"],
            ["RIMNICU VILCEA", "CRAIOVA", "BUCARESTE"],
            ["SIBIU", "PITESTI", "CRAIOVA"],
            ["RIMNICU VILCEA", "ORADEA", "FAGARAS", "ARAD"],
            ["LUGOJ", "ARAD"],
            ["VASLUI", "HIRSOVA", "BUCARESTE"],
            ["URZICENI", "IASI"],
            ["ORADEA", "ARAD"]
       ]

    def caminho(self, inicio, fim):
        """Metodo para encontrar caminho entre dois pontos.
        \ncaminho = caminho(cidade inicial, cidade final)
        \ncaminho recebe uma lista."""

        # manipular a FILA para a busca
        l1 = Lista()

        # cópia para apresentar o caminho (somente inserção)
        l2 = Lista()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,None)
        l2.insereUltimo(inicio,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            if atual is None: break

            ind = self.nos.index(atual.valor1)

            # varre todos as conexões dentro do grafo a partir de atual
            for i in range(len(self.grafo[ind])):

                novo = self.grafo[ind][i]
                flag = True  # pressuponho que não foi visitado

                # controle de nós repetidos
                for j in range(len(visitado)):
                    if visitado[j][0]==novo:
                        if visitado[j][1]<=(atual.valor2+1):
                            flag = False
                        else:
                            visitado[j][1]=atual.valor2+1
                        break
                
                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo, atual.valor2 + 1, atual)
                    l2.insereUltimo(novo, atual.valor2 + 1, atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.valor2+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        return caminho

        return "Caminho não encontrado."