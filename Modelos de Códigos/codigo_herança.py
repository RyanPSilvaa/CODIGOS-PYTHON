class Animal:
    def __init__(self, nome):
        self.nome = nome
    def respirar(self):
        print('Eu'+ self.nome+'Respirei...')
class Ave(Animal):
    def __init__(self, nome, cor_das_penas):
        self.nome = nome
        self.cor_das_penas = cor_das_penas
    def bater_asas(self):
        print('Eu'+ self.nome+'da pena'+self.cor_das_penas+',bati asas...')
class Urubu(Ave):
    def __init__(self, nome):
        super().__init__(nome, 'preta')
    def comerCarnica(self):
        print('Eu' + self.nome + ',comi carniça...')

class Galinha(Ave):
  def __init__(self, nome, cor, caipira):
    super().__init__(nome, cor)
    self.caipira = caipira
  def ciscar(self):
      if self.caipira == True:
          print("Eu, galinha " + self.nome,'Caipira' + ", cisquei.")
      else:
          print("Eu, galinha " + self.nome, 'de Granja' + ", cisquei.")
l = Galinha('Lilica','Azul', True)
l.ciscar()
m = Galinha('Canjica', 'Verde', False)
m.ciscar()
n = Galinha('Maura', 'Roxa', True)
n.ciscar()