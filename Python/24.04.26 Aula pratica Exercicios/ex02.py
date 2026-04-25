arr = []
for i in range(15):
    num = int(input("Digite um número: "))
    arr.append(num)

x = int(input("Digite um numero para saber se ele está na lista: "))

if x in arr:
    print(f"O número {x} está na lista.")
else:
    print(f"O número {x} não está na lista.")