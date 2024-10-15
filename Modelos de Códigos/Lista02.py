##########################################
#               Conjunto                 #
##########################################
conjunto = set()
conjunto2 = {7,2,3,9}
#print(type(conjunto2))

#add
conjunto.add(6)
conjunto.add(1)
conjunto.add(9)
conjunto.add(6)
#print(conjunto)

#remove
#conjunto.remove(1)

#union (une os dois conjuntos)
conjunto3 = conjunto.union(conjunto2)
#print(conjunto3)

#len(conjunto)
print(len(conjunto))