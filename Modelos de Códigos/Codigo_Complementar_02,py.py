class Pessoa:
    def __init__(self, nome, pai = None, mae = None, conjuge = None):
        self.nome = nome
        self.pai = pai
        self.mae = mae
        self.conjuge = conjuge
        self.filhos = []

    def mostrar_nome_conjuge(self):
        if self.conjuge is not None:
            print('Conjuge:', self.conjuge.nome)
        else:
            print('Não existe :(')

    def mostrar_nome_da_avo_paterna(self):
        if self.pai is not None and self.pai.mae is not None:
            print('Avó paterna:', self.pai.mae.nome)
        else:
            print('Não existe :(')

    def adicionarFilho(self, filho):
        self.filhos.append(filho)
        filho.pai = self

    def mostrar_filhos(self):
        if len(self.filhos) == 0:
            print(self.nome, 'não possui filhos')
        else:
            print('Filho de:', self.nome)
            #foreach
            for filho in self.filhos:
                print(filho.nome)
            #for i in range(len(self.filhos)):
                #print(self.filhos[i].nome)

    def mostrar_nome_do_avo_materno(self):
        if self.mae.pai is not None and self.mae.pai is not None:
            print('Avô materno:', self.mae.pai.nome)
        else:
            print('Não Existe :(')


p4 = Pessoa('Maria')
p3 = Pessoa('Joaquim')
p2 = Pessoa('Ivanice',pai = p3, mae = p4)
p1 = Pessoa('Ryan', mae = p2)
p5 = Pessoa('Pedro')

p1.adicionarFilho(p5)
p1.adicionarFilho(p5)
p1.mostrar_filhos()