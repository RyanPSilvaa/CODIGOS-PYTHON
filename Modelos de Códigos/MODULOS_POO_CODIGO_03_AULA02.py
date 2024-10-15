def fatorial(numero):
    f = 1
    c = 1
    while c <= numero:
        f *= c
        c += 1
    return f

a = fatorial(5)
print(a)