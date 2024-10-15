from mysql.connector import connect

conexao = connect(host='localhost', user='root', password='2106', database='ap1')
print('conexão aberta')
cursor = conexao.cursor()
cursor.execute('UPDATE produto SET preco_unitario = 20.25 WHERE nome = "Havaianas"')
conexao.commit()

cursor.close()
conexao.close()

# cursor.execute('SELECT nome FROM cidade') # --> consulta no Workbench#
# resultado = cursor.fetchall() # --> Traz o registro da consulta
# 'SELECT nome FROM cidade WHERE codigo = %s AND estado=%s',[cod, est]
# SELECT cliente.codigo, cliente.nome FROM cliente, cidade '+'WHERE cliente.cod_cidade = cidade.codigo AND '+'cidade.estado=%s',[est]#
# 'SELECT codigo, cliente WHERE %s',[termo]