# Exemplo 1:
# - Mostrar uma mensagem caso o
#   usuário não digite um inteiro
#   usando tratamento geral
#try:
#  v = int(input('Digite um número inteiro:'))
#  r = v * v
#  print('Quadrado de', v,'é', r)
#except:
#  print('Erro!')
#print('Fim do programa')
#"=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="#
# Exemplo 2.a:
# - Crie um programa para calcular
#   a divisão de dois números digitados
#   pelo usuário. Digite os valores acima.
#   Mostrar mensagem geral para ambos os erros: erro.
#try:
#    valor1 = int(input('Digite um número:'))
#    valor2 = int(input('Digite um número:'))
#    r = valor1 / valor2
#    print(r)
#except (ValueError, ZeroDivisionError):
#    print('Erro! Digite um valor inteiro.')
#except ZeroDivisionError:
#    print('Erro! Divisão por zero é inválida.')
from mysql.connector import connect, DatabaseError,ProgrammingError, IntegrityError

def error_host():
    h = input('Digite o Host:')
    u = input('Digite o User:')
    s = input('Digite a Senha:')
    b = input('Digite o Banco de Dados:')
    conexao = connect(host='localhost',
                      user='root',
                      password='2106',
                      database='aula040624')
    conexao.close()

https://colab.research.google.com/drive/1VyeaP2xSCoUu5_y13WX9XjxT2GatN99m#scrollTo=La5ps0BERpP1