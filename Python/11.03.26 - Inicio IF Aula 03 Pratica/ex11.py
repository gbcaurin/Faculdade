#Ler dois numeros e descobrir se eles estão na origem, no eixo X, no eixo Y ou em qual quadrante estão.  
x = float(input("Digite um número X: "))
y = float(input("Digite outro número Y: "))
if x == 0 and y == 0:
    print("Os números estão na origem.(0,0)")
if x == 0 and y != 0:
    print("Os números estão no eixo Y.")
if x != 0 and y == 0:
    print("Os números estão no eixo X.")
if x > 0 and y > 0:
    print("Os números estão no primeiro quadrante.")
if x < 0 and y < 0:
    print("Os números estão no terceiro quadrante.")
if x < 0 and y > 0:
    print("Os números estão no segundo quadrante.")
if x > 0 and y < 0:
    print("Os números estão no quarto quadrante.")