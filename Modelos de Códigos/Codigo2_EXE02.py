class Estudante():
    def __init__(self, nome, AP1, AP2, PF):
        self.nome = nome
        self.AP1 = AP1
        self.AP2 = AP2
        self.PF = PF
    def mostrarNota(self):
        nota = (self.AP1 + self.AP2 + self.PF) / 3
        if nota >= 6:
            print('Aprovado(a)')
        else:
            print('Reprovado(a)')

estudante1 = Estudante('Amanda', 5.2, 6.9, 7.1)
estudante1.mostrarNota()
estudante2 = Estudante('Bruno', 9.1, 4.3, 8.2)
estudante2.mostrarNota()
estudante3 = Estudante('Carol', 5.0, 6.5, 3.1)
estudante3.mostrarNota()