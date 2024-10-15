# criar um programa para calcular o IMC
# de uma pessoa sabendo-se seu peso(em kg)
# sua altura (em m) IMC = Peso / Altura*2

altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))
IMC = peso / (altura*altura)
print("Seu IMC é igual à:", IMC)