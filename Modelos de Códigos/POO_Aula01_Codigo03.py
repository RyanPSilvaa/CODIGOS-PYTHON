# criar um programa para calcular o IMC
# de uma pessoa sabendo-se seu peso(em kg)
# sua altura (em m) IMC = Peso / Altura²
# pessoa está com peso normal se
# IMC esteja em 20 e 25
# IMC = peso / altura²
altura = float(input("Digite sua altura:"))
idealMinimo = altura * altura * 20
idealMaximo = altura * altura * 25
print("Peso Ideal mínimo é:", idealMinimo, "Peso Ideal máximo é", idealMaximo)
