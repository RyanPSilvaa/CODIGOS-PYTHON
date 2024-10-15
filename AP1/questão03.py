class Categoria:
    def __init__(self, nome, orcamento):
        self.nome = nome
        self.orcamento = orcamento

class Despesa:
    def __init__(self, nome, descricao, valor, pago = 0):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.pago = pago

    def mostrar_dados(self):
        print('Categoria:', self.nome)
        print('Descrição: ',self.descricao)
        print('Valor: ', self.valor)
        if self.pago >= self.valor:
            print('Situação: => Pago', self.pago)
        else:
            print('Situação: => Pendente',self.valor - self.pago)

    def registrar_pagamento(self, pagamento):
        self.pago += pagamento


a = Categoria('Consumo', 450)
a1 = Categoria('Higiene', 80)
a2 = Categoria('Lazer', 200)

b = Despesa('Consumo','Rancho de 04/2024', 292.75, a)
c = Despesa('Viagem','Viagem de Férias', 656.06, a2)
d = Despesa('Consumo','Gasolina de 04/2024', 339.56, a)
e = Despesa('Higiene','Barbearia de 06/04/2024', 31.0, a1)

b.registrar_pagamento(300)
c.registrar_pagamento(800)
d.registrar_pagamento(500)
e.registrar_pagamento(50)
b.mostrar_dados()
c.mostrar_dados()
d.mostrar_dados()
e.mostrar_dados()