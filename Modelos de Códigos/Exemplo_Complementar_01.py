class Conta:
    def __init__(self, agencia, conta, limite = 0):
        self.agencia = agencia
        self.conta = conta
        self.limite = limite
        self.saldo = 0
        self.bandeira = []
    def depositarValor(self, valor):
        self.saldo += valor
    def mostrar_saldo(self):
        print(self.saldo)

    def adicionarBandeira(self, bandeiras):
        self.bandeira.append(bandeiras)

    def mostrarBandeiras(self):
        if len(self.bandeira) == 0:
            print(self.conta, 'Não possui nenhuma bandeira')
        else:
            print('bandeira', self.bandeira)
            for bandeiras in self.bandeira:
                print(bandeiras.bandeira)

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print('saque negado!')

conta = Conta('123', '4567-8', 1000)
conta.adicionarBandeira('Mastercard')
conta.mostrarBandeiras()