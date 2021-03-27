class Processo:
    
    def __init__(self, descricao, custo, decisao, status, cod):
        self._descricao = descricao
        self._custo = custo
        self._decisao = decisao
        self._status = status
        self._cod = cod
        self._prox = None

    # GETTER AND SETTERS

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, nova_descricao):
        self._descricao = nova_descricao

    def get_custo(self):
        return self._custo

    def set_custo(self, novo_custo):
        self._custo = novo_custo

    def get_decisao(self):
        return self._decisao

    def set_decisao(self, nova_decisao):
        self._decisao = nova_decisao

    def get_status(self):
        return self._status

    def set_status(self, novo_status):
        self._status = novo_status

    def get_cod(self):
        return self._cod

    def set_cod(self, novo_cod):
        self._status = novo_cod


    def get_prox(self):
        return self._prox
    
    def set_prox(self, novo):
        self._prox = novo

    #OUTROS METODOS
    def incrementa_custo(self, novo_custo):
        self._custo += novo_custo