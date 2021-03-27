from Processo import Processo


class ListaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class Lista:
    
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def mostrar_elemento(self):
        if self.vazia():
            raise FilaException('A lista está vazia')

        return self.__inicio

    def tamanho(self):
        return self.__tamanho

    def vazia(self):
        return self.__tamanho == 0

    def adicionar(self, descricao, custo, decisao, status, cod):
        novo = Processo(descricao, custo, decisao, status, cod)
        aux = self.__inicio

        if aux == None:
            self.__inicio = novo

        else:
            while aux.get_prox() != None:
                aux = aux.get_prox()

            aux.set_prox(novo)

        self.__tamanho += 1 