from mysql.connector import connect

conexao = connect(host='localhost', user='root', password='2106', database='banco_da_prova')
print('conexão aberta!')

cursor = conexao.cursor()
cursor.execute('SELECT nome FROM produto WHERE preco_unitario < 10')
resultado = cursor.fetchall()
print(resultado)

conexao.close()
print('Conexão fechada!')