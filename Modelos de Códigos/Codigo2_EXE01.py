idade = int(input('Digite a idade do atleta:'))

if idade == 4 or idade == 5:
    print('classe A')
elif 7 <= idade <= 12:
    print('Classe B')
elif idade == 15 or idade == 17:
    print('Classe C')
elif 18 <=idade <= 25:
    print('Classe D')
elif idade >= 26:
    print('Classe E')
else:
    print('Não está em nenhuma classe!')