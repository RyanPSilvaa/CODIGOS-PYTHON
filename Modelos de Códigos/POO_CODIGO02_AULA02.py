# versão orientada a objetos
class Vendedor():
  def __init__(self, v, m, n): #construtor
    self.vendas = v
    self.meta = m
    self. nome = n
  def cumpriuVendas(self):
    if self.vendas >= self.meta:
      print(self.nome, 'Cumpriu a meta!')
    else:
      print(self.nome, 'Não Cumpriu meta')
# classe somente com a declaração de atributos
m = Vendedor(603, 500, 'Maria')
c = Vendedor(350, 500,'Carlos')
l = Vendedor(490, 500, 'Lenir')

m.cumpriuVendas()
c.cumpriuVendas()
l.cumpriuVendas()