anosexperiencia = int(input("digite os anos de experiência:"))
idade = int(input("Digite a sua idade:"))
numerodefilhos = int(input("Digite o número de filhos:"))
horastrabalhadas = int(input("Digite as horas trabalhadas:"))

f = (numerodefilhos + horastrabalhadas)/anosexperiencia*idade
print("Seu indice de felicidade é:", f)