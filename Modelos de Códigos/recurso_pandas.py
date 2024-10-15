from pandas import DataFrame
dados = {}
dados['cod'] = ['62', '47', '90']
dados['Nome'] = ['Maria', 'Ana', 'Caio']
dados['Telefone'] = ['98403-4103', '98403-4103', '98403-4103']

d = DataFrame(dados)
d.to_excel('exemplo.xlsx')