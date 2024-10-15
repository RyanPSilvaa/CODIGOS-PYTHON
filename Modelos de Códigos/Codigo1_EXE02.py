class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def mostrarIdade(self):
        if self.idade < 18:
            print(self.nome, ' de Menor')
        else:
            print(self.nome, ' de Maior')

n1 = Pessoa('Ana', 16)
n2 = Pessoa('Jorge', 25)
n1.mostrarIdade()
n2.mostrarIdade()