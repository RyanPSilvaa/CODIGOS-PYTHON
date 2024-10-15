#Criar uma calculadora com
# estrutura condicional While

x = int(input())
y = int(input())
i = 1
j = 1
while i <= x:
  j = i
  while j <= y:
    print(i,"*",j,"=",i*j)
    j+= 1
  i+=1

#Código com estrutura For
#tabuada = int(input())
#for count in range(4):
#  print("%d * %d = %d" % (tabuada, count+1, tabuada*(count+1)))