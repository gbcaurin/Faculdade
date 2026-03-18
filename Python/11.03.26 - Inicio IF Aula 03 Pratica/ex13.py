#Ler os coeficientes de uma equação do segundo grau e calcular as raízes.  
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
delta = (b ** 2) - (4 * a * c)
if delta < 0 or a == 0:
    print("A equação não possui raízes reais.")
else:
    b_plus = (-b + (delta ** 0.5)) / (2 * a)
    b_minus = (-b - (delta ** 0.5)) / (2 * a)
    print(f"As raízes da equação são: {b_plus} e {b_minus}.")