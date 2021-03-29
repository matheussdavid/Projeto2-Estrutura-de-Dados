from Processo import Processo

class PilhaException(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class Pilha:
  def __init__(self):
    self._topo = None
    self._tamanho = 0

  @property
  def mostrar_elemento(self):
    if self.vazio():
      raise PilhaException('A pilha está vazia')

    return self._topo.dado
  
  def vazio(self):
    return self._tamanho == 0

  def tamanho(self):
    return self._tamanho
  
  def adicionar(self, processo):
    processo.set_prox(self._topo)
    self._topo = processo
    self._tamanho += 1

  def remover(self):
    if self.vazio():
      raise PilhaException('A pilha está vazia')
    self._topo = self._topo.get_prox()
    self._tamanho -= 1

  def __str__(self):
    saida = "Pilha: ["
    p = self._topo

    while p != None:
      saida += f'{p.get_descricao(), p.get_custo(), p.get_decisao(), p.get_status(), p.get_cod()}'
      p = p.get_prox()

      if p != None:
        saida += ', '

    saida += ']'
    return saida

  def imprimir(self):
        saida = '---- PROCESSOS ----\n\n'
        p = self._topo
        while p != None:
            saida += f'{p.get_descricao(), p.get_custo(), p.get_decisao(), p.get_status(), p.get_cod()}'
            p = p.get_prox()
            if p != None:
                saida += '\n'
        return saida
  