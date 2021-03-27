from Processo import Processo

class ListaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class Lista:
    
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0
        
    def __str__(self):
        saida = 'Lista:\n[\n'
        p = self.__inicio

        while p != None:
            saida += f'{p.get_cod(), p.get_descricao(), p.get_custo(), p.get_decisao(), p.get_status()}'
            p = p.get_prox()

            if p != None:
                saida += ',\n'

        saida += '.\n]'
        return saida
    
    @property
    def inicio(self):
        if self.vazia():
            raise FilaException('A Lista está vazia')
        return self.__inicio
    
    def vazia(self):
        return self.__tamanho == 0
    
    def tamanho(self):
        return self.__tamanho
    
    def mostrar_elemento(self, cod):
        if self.vazia():
            raise FilaException('A lista está vazia')

        cont = 0
        p = self.__inicio
        while (cont <= self.tamanho()) and p!= None:
            if( p.get_dado() == cod):
                return print(p)
            p = p.get_prox()
            cont += 1    
        return print('O código informado não bate com algum dos códigos cadastrados!')

    def vazia(self):
        return self.__tamanho == 0

    def imprimir(self):
        saida = '---- PROCESSOS ----\n\nCódigo  Status\n'
        p = self.__inicio
        while p != None:
            saida += f'{p.get_dado()}    {p.get_custo()}'
            p = p.prox
            if p != None:
                saida += '\n'
        return print(saida)
    
    def adicionar(self, descricao, custo, decisao, status, cod, posicao):
        novo = Processo(descricao, custo, decisao, status, cod)

        if self.vazia():
            novo.set_prox(self.__inicio)
            self.__inicio = novo
        elif posicao <= 0:
            raise FilaException('O valor da posição é inválido, tente novamente') 
        elif posicao == 1:
            novo.set_prox(self.__inicio)
            self.__inicio = novo
        else:
            posicao -=1
            p = self.__inicio
            q = None
            cont = 0
            while (cont < posicao) and p!= None:
                q = p
                p = p.get_prox()
                cont += 1
            q.set_prox(novo)
            novo.set_prox(p)
        self.__tamanho += 1
    
    def remover(self, posicao): 
        
        if self.vazia():
            raise FilaException('A fila está vazia')
        elif (posicao > self.tamanho()) or posicao <= 0:
            raise FilaException('Valor inválido, a lista é menor do que o valor informado')
        elif posicao == 1:
            self.__inicio = self.__inicio.get_prox()
        else:
            posicao -= 1  
            p = self.__inicio
            q = None
            cont = 0
            while (cont != posicao) and p!= None:
                q = p
                p = p.get_prox()
                cont += 1
            q.set_prox(p.get_prox())
        self.__tamanho -= 1

    def busca(self, cod, posicao):
        cont = 0
        p = self.__inicio
        while (cont != posicao) and p!= None:
            if( p.get_cod() == cod):
                return print(p)
            p = p.get_prox()
            cont += 1    
        return print('O código informado não bate com algum dos códigos cadastrados!')
    
    def busca_processo(self, cod):
        cont = 0
        p = self.__inicio
        while (cont <= self.tamanho()) and p!= None:
            if( p.get_cod() == cod):
                return p
            p = p.get_prox()
            cont += 1    
        return print('O código informado não bate com algum dos códigos cadastrados!')

if __name__ == '__main__':

    l = Lista()

    l.adicionar("Calunia", "1000", "favoravel", "finalizado", "001", 1)
    print(l)
    l.adicionar("Calunia", "1000", "favoravel", "finalizado", "002", 1)
    print(l)
    print("\n\n\n")
    print(l.busca_processo("002"))    