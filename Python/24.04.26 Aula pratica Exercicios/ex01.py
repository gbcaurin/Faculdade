arr = []
for i in range(10):
    num = int(input("Digite um número: "))
    arr.append(num)
print("Números digitados:", *arr)