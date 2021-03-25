class Advogado:
    
    def __init__(self, cod_oab):
        self._cod_oab = cod_oab
        self._processosL = None
        self._processosP = None
        self._processosF = None

    # GETTER AND SETTERS
    def get_cod_oab(self):
        return self._cod_oab

    def set_cod_oab(self, novo_cod_oab):
        self._cod_oab = novo_cod_oab
        
    # OUTROS METODOS
    #     
    def maior_custo():
        pass

    def menor_custo():
        pass

    def incrementa_custo_processo(cod, valor):
        pass

    def adicionar_processo_P(novo_processo):
        pass

    def adicionar_processo_L(novo_processo, posicao):
        pass

    def adicionar_processo_F(novo_processo):
        pass

    def remover_processo_P():
        pass

    def remover_processo_L(posicao):
        pass

    def remover_processo_F():
        pass

    def busca_processo(cod):
        pass

    def ordena_processos():
        pass

    def imprimir_processos():
        pass

    def mostrar_tam_processosL():
        pass
    
    def mostrar_tam_processosP():
        pass

    def mostrar_tam_processosF():
        pass