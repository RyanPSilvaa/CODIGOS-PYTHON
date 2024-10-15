class Pessoa():
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def mostrarDados(self):
        print('Nome:', self.nome)
        print('Peso:', self.peso,'kg')
        print('Altura:', self.altura,'m')
        IMC = self.peso / (self.altura**2)
        if IMC < 18.5:
            print(IMC,'Abaixo')
        elif IMC >= 18.5 and IMC < 24.9:
            print(IMC,'Normal')
        elif IMC >= 25 and IMC < 29.9:
            print(IMC,'Acima do peso')
        else:
            print(IMC,'Obesidade')

pessoa1 = Pessoa('Fulano1', 52.2, 1.60)
pessoa1.mostrarDados()
pessoa2 = Pessoa('Fulano2', 100.2, 1.59)
pessoa2.mostrarDados()
pessoa3 = Pessoa('Fulano3', 23.2, 1.70)
pessoa3.mostrarDados()