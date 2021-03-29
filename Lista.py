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
            raise ListaException('A Lista está vazia')
        return self.__inicio
    
    def set_inicio(self, novo):
        self.__inicio = novo
    
    def vazia(self):
        return self.__tamanho == 0
    
    def tamanho(self):
        return self.__tamanho
    
    def mostrar_elemento(self, posicao):
        if self.vazia():
            raise ListaException('A lista está vazia')

        cont = 0
        p = self.__inicio
        while (cont < posicao) and p!= None:
            p = p.get_prox()            
            cont += 1
        return p    

    def imprimir(self):
        saida = '---- PROCESSOS ----\n\n'
        p = self.__inicio
        while p != None:
            saida += f'{p.get_descricao(), p.get_custo(), p.get_decisao(), p.get_status(), p.get_cod()}'
            p = p.get_prox()
            if p != None:
                saida += '\n'
        return saida
    
    def adicionar(self, processo, posicao):

        if self.vazia():
            processo.set_prox(self.__inicio)
            self.__inicio = processo
        elif posicao <= 0:
            raise ListaException('O valor da posição é inválido, tente novamente') 
        elif posicao == 1:
            processo.set_prox(self.__inicio)
            self.__inicio = processo
        else:
            posicao -=1
            p = self.__inicio
            q = None
            cont = 0
            while (cont < posicao) and p!= None:
                q = p
                p = p.get_prox()
                cont += 1
            q.set_prox(processo)
            processo.set_prox(p)
        self.__tamanho += 1
    
    def remover(self, posicao):
        
        if self.vazia():
            raise ListaException('A fila está vazia')
        elif (posicao > self.tamanho()) or posicao <= 0:
            raise ListaException('Valor inválido, a lista é menor do que o valor informado')
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
    
    def buscar_processo(self, cod):
        cont = 0
        p = self.__inicio
        while (cont <= self.tamanho()) and p!= None:
            if( p.get_cod() == cod):
                return p
            p = p.get_prox()
            cont += 1    
        return print('O código informado não bate com algum dos códigos cadastrados!')
    
    def ordenar(self):
        tamanho = self.tamanho()
        for i in range(tamanho - 1):
            atual = self.__inicio
            proximo = atual.get_prox()
            anterior = None
            while proximo != None:
                if atual.get_cod() > proximo.get_cod():
                    if anterior == None:
                        anterior = atual.get_prox()
                        proximo = proximo.get_prox()
                        anterior.set_prox(atual)
                        atual.set_prox(proximo)
                        self.set_inicio(anterior)
                    else:
                        temp = proximo
                        proximo = proximo.get_prox()
                        anterior.set_prox(atual.get_prox())
                        anterior = temp
                        temp.set_prox(atual)
                        atual.set_prox(proximo)
                else:
                    anterior = atual
                    atual = proximo
                    proximo = proximo.get_prox()
            i += 1
        return self.imprimir()
    
    def maior_custo(self):
        custo = 0
        status = ""
        cont = 0
        p = self.__inicio
        while (cont != self.tamanho()) and p!= None:
            if( p.get_custo() > custo):
                custo =  p.get_custo()
                status = p.get_status()
            p = p.get_prox()
        return f'Custo: R${custo}\nStatus: {status}.'

    def menor_custo(self):
        custo = 99999999999999999
        status = ""
        cont = 0
        # TROQUEI TUDO QUE TINHA PROCESSOSL POR SELF 
        p = self.__inicio
        while (cont != self.tamanho()) and p!= None:
            if( p.get_custo() < custo):
                custo =  p.get_custo()
                status = p.get_status()
            p = p.get_prox()
        return f'Custo: R${custo}\nStatus: {status}.'

        
    def imprimir_processos(self):
        saida = '---- PROCESSOS ----\n\nCódigo  Status\n'
        p = self.__inicio
        while p != None:
            saida += f'{p.get_cod()}    {p.get_status()}'
            p = p.get_prox()
            if p != None:
                saida += '\n'
        return saida

# if __name__ == '__main__':

#     l = Lista()

#     processoL1 = Processo('Civíl', 1000, 'Deferido', 'Transitado em Julgado', '021')
#     processoL2 = Processo('Civíl', 2000, 'Indeferido', 'Prazo para Recurso', '022')
#     processoL3 = Processo('Civíl', 3000, 'Deferido', 'Embargos declaratórios','023')
#     processoL4 = Processo('Civíl', 4000, 'Indeferido', 'Arquivado', '024')
#     processoL5 = Processo('Civíl', 5000, 'Deferido', 'Em execução', '025')



#     l.adicionar(processoL1, 5)
#     l.adicionar(processoL2, 4)
#     l.adicionar(processoL3, 3)
#     l.adicionar(processoL4, 2)
#     l.adicionar(processoL5, 1)
#     print(l)
#     print("\n\n\n")
#     print(l.tamanho())
#     print(l.ordenar())

