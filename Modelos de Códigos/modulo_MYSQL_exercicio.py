from mysql.connector import *
sql = ('select cliente.nome, cidade.nome, estado from cliente,' +\
        'cidade where cliente.cod_cidade = cidade.codigo and cidade.estado = %s')

con = connect(host='192.168.43.56', user='user1405', password='poo', database='aula1405')
estado = input('Digite um estado:')
c = con.cursor()
c.execute(sql,[estado])
registros = c.fetchall()
for cliente in registros:
    print('Cliente',cliente)
print('Conectado')
con.close()