# Os números inteiros menores
# que um número inteiro digitado
# pelo usuário
valor = int(input())
contador = 1
soma = 0
while contador < valor:
  soma += contador
  contador += 1
print(soma)