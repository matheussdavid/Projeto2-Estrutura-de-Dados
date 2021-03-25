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
  
  def adicionar(self, descricao, custo, decisao, status, cod):
    processo = Processo(descricao, custo, decisao, status, cod)
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
    print(self.__str__())
  
  # def modificar(self, novoValor):
  #   if self.vazia():
  #     raise PilhaException('A pilha está vazia')
  #   self._topo.dado = novoValor


if __name__ == '__main__':
  p = Pilha()



p.adicionar("Calunia", 1000, "favorável", "deferido","001")
p.adicionar("Calunia", 1000, "favorável", "deferido","002")
p.adicionar("Calunia", 1000, "favorável", "deferido","003")
p.adicionar("Calunia", 1000, "favorável", "deferido","004")



p.remover()
print(p)

p.remover()
print(p)
