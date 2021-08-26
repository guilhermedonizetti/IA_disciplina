from lista_encadeada import Nos

class Lista:

    def __init__(self):
        self.head = None
        self._tamanho = 0
    
    def adicionar_valor(self, valor):
        if self.head:
            ponteiro = self.head
            while(ponteiro.next):
                ponteiro = ponteiro.next
            ponteiro.next = Nos(valor)
        else:
            self.head = Nos(valor)
        self._tamanho += 1
    
    def __len__(self):
        return self._tamanho
    
    def get(self, indice):
        pass

    def set(self, indice, valor):
        pass

    #Deve-se continuar a gerar o algoritmo da lista