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
        
    # OUTROS METODOS - LISTA   
    def maior_custo(self):
        pass

    def menor_custo(self):
        pass

    def incrementa_custo_processo(self, cod, valor):
        pass

    def busca_processo(self, cod):
        pass

    def ordena_processos(self):
        pass

    def imprimir_processos(self):
        pass

    def adicionar_processo_L(self, novo_processo, posicao):
        pass

    def remover_processo_L(self, posicao):
        pass

    def mostrar_tam_processosL(self):
        return self._processosL.tamanho()


    # OUTROS METODOS - PILHA
    def adicionar_processo_P(self, descricao, custo, decisao, status, cod):
        self._processosP.adicionar(descricao, custo, decisao, status, cod)

    def remover_processo_P(self):
        self._processosP.remover()  

    def mostrar_tam_processosP(self):
        return self._processosP.tamanho()


    # OUTROS METODOS - FILA    
    def adicionar_processo_F(self, descricao, custo, decisao, status, cod):
        self._processosF.adicionar(descricao, custo, decisao, status, cod)
      
    def remover_processo_F(self):
        self._processosF.remover()  

    def mostrar_tam_processosF(self):
        return self._processosF.tamanho()



if __name__ == '__main__':

    safado = Advogado("01")

    safado.adicionar_processo_P("Calunia", "1000", "favoravel", "finalizado", "001")
    safado.adicionar_processo_P("Calunia", "1000", "favoravel", "finalizado", "002")
    print(safado.mostrar_tam_processosP())
    safado.remover_processo_P()
    print(safado.mostrar_tam_processosP())
    print(safado.get_processosP())
    print(safado.mostrar_tam_processosL())