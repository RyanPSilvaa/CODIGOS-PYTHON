numero = int(input())
contador = 1
acumulador = 1
while contador <= numero:
  acumulador *= contador
  contador += 1
print(acumulador)