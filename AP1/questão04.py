class Funcionario:

    def __init__(self, nome, chefe = None):
        self.nome = nome
        self.chefe = chefe
        self.subordinados = []

        if self.chefe is not None:
            self.chefe.subordinados.append(self)

    def sou_chefia_de (self, funcionario):
        count = 0
        for i in range(len(self.subordinados)):
            if funcionario == self.subordinados[i]:

                print(f"Eu {self.nome}, sou chefe de: {funcionario.nome}")
                count = 1
        if count == 0:
            print(f"Eu {self.nome}, não sou chefe de: {funcionario.nome}")

a = Funcionario("Ana")
t = Funcionario("Tereza", a)
m = Funcionario("Manoel", a)
p = Funcionario("Pedro", m)

t.sou_chefia_de(a)
a.sou_chefia_de(m)