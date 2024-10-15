#r -> usado para ler algo
#w -> usado para escrever algo
#r+ -> usado para ler e escrever algo
#a -> usado para acrescentar algo

#1
var1 = 'Ryan'
with open('ex1.txt','w') as arquivo:
    for nome in var1:
        arquivo.write(str(nome))
        arquivo.close()

#2
var2 = 'Pereira'
with open('ex2.txt','w') as arquivo:
    for sobrenome in var2:
        arquivo.write(str(sobrenome))

#3
from zipfile import ZipFile
with ZipFile("arquivos.zip", "w") as zip:
  zip.write("ex1.txt")
  zip.write("ex2.txt")