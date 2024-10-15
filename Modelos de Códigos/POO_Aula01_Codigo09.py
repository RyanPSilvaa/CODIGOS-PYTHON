qtd = int(input())
contador = 1
menor = 0
while contador <= qtd:
  numero = int(input())
  menor = numero
  if contador == 1 or menor > numero:
    menor = numero
    print(menor)
  contador += 1
print(menor)