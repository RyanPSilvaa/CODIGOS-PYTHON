from mysql.connector import connect

conexao = connect(host='localhost', user='root', password='2106', database='banco_da_prova')
cursor = conexao.cursor()
def questao2a():
    cursor.execute("select P.nome as Nome, C.nome as Categoria from produto P, categoria C where C.codigo = P.cod_categoria and P.estoque = 0;")
    print(cursor.fetchall())
    conexao.close()
questao2a()

def questao2b():
    alteracao = "update produto set preco_unitario = %s where produto.codigo = %s"
    codigo_produto = input("Digite um código de produto:")
    novo_valor = input("Diigite o novo preço do produto: ")
    cursor.execute(alteracao, [novo_valor, codigo_produto])
    conexao.commit()
    print("Valor alterado\nNovos valores:")
    cursor.execute("select * from produto")
    print(cursor.fetchall())
questao2b()