n = int(input("Quantos numeros voce quer somar?: "))
x = 2
y = 3
z = x + y

i = 0

while i < n:
    print(f"{x} + {y} = {z}")
    x = y
    y = z
    z = x + y
    i += 1