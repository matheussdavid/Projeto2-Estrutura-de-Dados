from Processo import *
from Feeders import *
from Fila import Fila
from Pilha import Pilha
from Lista import Lista

class Advogado:
    def __init__(self, cod_oab):
        self._cod_oab = cod_oab
        self._processosL = Lista()
        self._processosP = Pilha()
        self._processosF = Fila()

    # GETTER AND SETTERS
    def get_cod_oab(self):
        return self._cod_oab

    def set_cod_oab(self, novo_cod_oab):
        self._cod_oab = novo_cod_oab
    
    def get_processosP(self):
        return self._processosP

    def get_processosF(self):
        return self._processosF

    def get_processosL(self):
        return self._processosL  
        
    # OUTROS METODOS - LISTA   
    def maior_custo(self):
        return self._processosL.maior_custo()

    def menor_custo(self):
        return self._processosL.menor_custo()

    def incrementa_custo_processo(self, cod, valor):
        processo = self._processosL.buscar_processo(cod)
        processo.incrementa_custo(valor)

    def busca_processo(self, cod):
        processo = self.get_processosL().buscar_processo(cod)
        return processo

    def ordena_processos(self):
        return self._processosL.ordenar()
    

    def imprimir_processos(self):
        return self._processosL.imprimir_processos()

    def adicionar_processo_L(self, processo, posicao):
        self._processosL.adicionar(processo, posicao)

    def remover_processo_L(self, posicao):
        return self._processosL.remover(posicao)

    def mostrar_tam_processosL(self):
        return self._processosL.tamanho()


    # OUTROS METODOS - PILHA
    def adicionar_processo_P(self, processo):
        self._processosP.adicionar(processo)

    def remover_processo_P(self):
        self._processosP.remover()  

    def mostrar_tam_processosP(self):
        return self._processosP.tamanho()

    # OUTROS METODOS - FILA    
    def adicionar_processo_F(self, processo):
        self._processosF.adicionar(processo)
    
    def remover_processo_F(self):
        self._processosF.remover()  

    def mostrar_tam_processosF(self):
        return self._processosF.tamanho()

    def __str__(self):
        return f'Advogado OAB: {self.get_cod_oab()}\n\nProcessos Penais (ProcessosP):\n\n{self.get_processosP().imprimir()}\n\n\nProcessos Trabalhistas (ProcessosF):\n\n{self.get_processosF().imprimir()}\n\n\nProcessos Cíveis (ProcessosL):\n\n{self.get_processosL().imprimir()}\n\n' 

# if __name__ == '__main__':

    # print(advogado1.get_processosF().imprimir())
    # print(advogado1.get_processosP().imprimir())
    # print(advogado1.get_processosL().imprimir())
    # print(advogado1.get_processosP())

    # safado = Advogado("01")
    # safado.adicionar_processo_L("Calunia", "1000", "favoravel", "finalizado", "005", 1)
    # safado.adicionar_processo_L("Calunia", "1000", "favoravel", "finalizado", "004", 2)
    # safado.adicionar_processo_L("Calunia", "1000", "favoravel", "finalizado", "003", 3)
    # safado.adicionar_processo_L("Calunia", "1000", "favoravel", "finalizado", "001", 4)
    # safado.adicionar_processo_L("Calunia", "1000", "favoravel", "finalizado", "002", 5)
    
    # print(safado.mostrar_tam_processosL())
    # print(safado.imprimir_processos())
    # safado.ordena_processos()
    # print(safado.imprimir_processos())

    # safado.remover_processo_P()
    # print(safado.mostrar_tam_processosP())
    # print(safado.get_processosP())
    # print(safado.mostrar_tam_processosL())