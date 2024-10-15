class Aluno:
    def __init__(self,nome, AP1, E1, AP2, E2):
        self.nome = nome
        self.AP1 = AP1
        self.E1 = E1
        self.AP2 = AP2
        self.E2 = E2

    def mostrarDados(self):
        mee = (self.AP1 + self.E1 + self.AP2 + self.E2) / 2
        if mee == 7.5:
            print('Nome:', self.nome)
            print('MEE:', mee, '(Vai pra PF)')
        elif mee >= 8:
            print('Nome:', self.nome)
            print('MEE:', mee, '(Não vai pra PF)')
        else:
            print('Nome:', self.nome)
            print('MEE', mee, '(Reprovou!)')

aluno1 = Aluno('Fulano', 8.9, 2.75, 4.7, 1.75)
aluno1.mostrarDados()
aluno2 = Aluno('Fulano2', 3.2, 0.25, 5.1, 0.75 )
aluno2.mostrarDados()
aluno3  = Aluno('Fulano3', 2.3, 1.25, 3.0, 1.0)
aluno3.mostrarDados()