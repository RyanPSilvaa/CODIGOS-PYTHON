def Bissexto(ano):
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        return True
    return False

print(Bissexto(2024))
print(Bissexto(2100))
print(Bissexto(2000))