####################################################
# DICIONÁRIO
####################################################
# mapa (chave, valor)
dicionario = dict() # alternativo: {}

# __setitem__(k,v) (adiciona elemento no mapeamento)
dicionario.__setitem__('a', 6) # ou dicionario['a'] = 6
dicionario.__setitem__(6, 'a')
dicionario[5] = 'b'
dicionario['a'] = 8
print(dicionario)
print(dicionario[6])
# len(dict)
