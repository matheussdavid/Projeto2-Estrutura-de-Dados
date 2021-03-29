class FilaException(Exception):    
    def __init__(self,mensagem):
        super().__init__(mensagem)

class Node:
    def __init__(self, dado = None, custo = None):
        self.__dado = dado
        self.__custo = custo
        self.__prox = None
        
    def __str__(self):
        return f'Dado: {self.get_dado()}\nCusto: R${self.get_custo()}'

    def get_dado(self):
        return self.__dado

    def set_dado(self, novo):
        self.__dado = novo

    def get_custo(self):
        return self.__custo

    def set_custo(self, novo):
        self.__custo = novo

    def incrementa_custo(self, novo_custo):
        self.__custo += novo_custo
        
    # get
    @property
    def prox(self):
        return self.__prox

    # set
    @prox.setter
    def prox(self, novo):
        self.__prox = novo


class ListaE:

    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    @property
    def inicio(self):
        if self.vazia():
            raise FilaException('A Lista está vazia')
        return self.__inicio

    def vazia(self):
        return self.__tamanho == 0

    def tamanho(self):
        return self.__tamanho

    def inserir(self, dado, custo, posicao):
        novo = Node(dado, custo)
        aux = self.__inicio

        if self.vazia():
            novo.prox = self.__inicio
            self.__inicio = novo
        elif posicao <= 0:
            raise FilaException('O valor da posição é inválido, tente novamente') 
        elif posicao == 1:
            novo.prox = self.__inicio
            self.__inicio = novo
        else:
            posicao -=1
            p = self.__inicio
            q = None
            cont = 0
            while (cont < posicao) and p!= None:
                q = p
                p = p.prox
                cont += 1
            q.prox = novo
            novo.prox = p
        self.__tamanho += 1 

    def remover(self, posicao):
        if self.vazia():
            raise FilaException('A fila está vazia')
        elif (posicao > self.tamanho()) or posicao <= 0:
            raise FilaException('Valor inválido, a lista é menor do que o valor informado')
        elif posicao == 1:
            self.__inicio = self.__inicio.prox
        else:
            posicao -= 1  
            p = self.__inicio
            q = None
            cont = 0
            while (cont != posicao) and p!= None:
                q = p
                p = p.prox
                cont += 1
            q.prox = p.prox
        self.__tamanho -= 1  

    def __str__(self):
        saida = 'Lista: ['
        p = self.__inicio

        while p != None:
            saida += f'{p.get_dado()}'
            p = p.prox

        if p != None:
            saida += ', '

        saida += ']'
        return saida

    def imprimir(self):
        saida = '---- PROCESSOS ----\n\nCódigo  Status\n'
        p = self.__inicio
        while p != None:
            saida += f'{p.get_dado()}    {p.get_custo()}'
            p = p.prox
            if p != None:
                saida += '\n'
        return print(saida)

    def modificar(self, novoValor):
        if self.vazia():
            raise FilaException('A fila está vazia')
        
        self.__topo.dado = novoValor

    def maior_custo(self):
        pass
   
    def menor_custo(self):
        menor = 9999
        cont = 0
        p = self.__inicio
        while (cont != self.tamanho()) and p!= None:
            if( p.get_custo() < menor):
                menor =  p.get_custo()
            p = p.prox
        return menor
    
    def busca(self, cod):
        cont = 0
        p = self.__inicio
        while (cont <= self.tamanho()) and p!= None:
            if( p.get_dado() == cod):
                return print(p)
            p = p.prox
            cont += 1    
        return print('O código informado não bate com algum dos códigos cadastrados!')

        
    def incrementa_custo_processo(self, cod, valor):
        #A solução que está em Advogado é bem mais simples que essa
        cont = 0
        p = self.__inicio
        while (cont <= self.tamanho()) and p!= None:
            if( p.get_dado() == cod):
                p.incrementa_custo(valor)
                return print(f'Valor atualizado do Processo: R${p.get_custo()}')
            p = p.prox
            cont += 1           
        return print('O código informado não bate com algum dos códigos cadastrados!')

if __name__ == '__main__':

    l = ListaE()
    l.inserir("-10-", 9999, 10)
    l.inserir("-02-", 2, 1)
    l.inserir("-03-", 10000, 5)
    l.inserir("-01-", 10000, 1)
    print(l)
    print(l.tamanho())
    l.remover(5)
    print(l)
