from Processo import Processo

class FilaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class Fila:
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def __str__(self):
        saida = 'Fila: ['
        p = self.__inicio

        while p != None:
            saida += f'{p.get_descricao(), p.get_custo(), p.get_decisao(), p.get_status(), p.get_cod()}'
            p = p.get_prox()

            if p != None:
                saida += ', '

        saida += ']'
        return saida

    def imprimir(self):
        saida = '---- PROCESSOS ----\n\n'
        p = self.__inicio
        while p != None:
            saida += f'{p.get_descricao(), p.get_custo(), p.get_decisao(), p.get_status(), p.get_cod()}'
            p = p.get_prox()
            if p != None:
                saida += '\n'
        return saida

    def mostrar_elemento(self):
        if self.vazia():
            raise FilaException('A fila está vazia')

        return self.__inicio

    def tamanho(self):
        return self.__tamanho

    def vazia(self):
        return self.__tamanho == 0

    def adicionar(self, processo):
        novo = processo
        aux = self.__inicio

        if aux == None:
            self.__inicio = novo

        else:
            while aux.get_prox() != None:
                aux = aux.get_prox()
        
            aux.set_prox(novo)

        self.__tamanho += 1 

    def remover(self):
        if self.vazia():
            raise FilaException('A fila está vazia')

        self.__inicio = self.__inicio.get_prox()
        self.__tamanho -= 1  
    
#TESTANDO    
# if __name__ == '__main__':

#     f = Fila()

#     f.adicionar("Calunia", "1000", "favoravel", "finalizado", "001")
#     f.adicionar("Calunia", "1000", "favoravel", "finalizado", "002")    
#     f.adicionar("Calunia", "1000", "favoravel", "finalizado", "003")
#     f.adicionar("Calunia", "1000", "favoravel", "finalizado", "004")

#     print(f.tamanho())
#     print(f)

#     f.remover()
#     print(f)

#     f.remover()
#     print(f)

#     f.remover()
#     print(f)

#     f.remover()
#     print(f)

#     f.remover()
#     print(f)