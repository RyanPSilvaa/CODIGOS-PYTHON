a = int(input('Digite um valor para A:'))
b = int(input('Digite um valor para B:'))
c = int(input('Digite um valor para C:'))
x = c
while x <= c and x >= b:
    if x % a == 0 and x > 0:
        print(x)
    x -= 1