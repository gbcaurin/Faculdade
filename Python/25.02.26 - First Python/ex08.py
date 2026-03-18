#Elaborar um programa que dado um valor X de um concurso em reais, ele imrpima a quantia ganha por cada jogador.
value = float(input("Digite o valor total em R$:"))
fst = value * 0.46
scnd = value * 0.32
thrd=  value * 0.22
print("O primeiro colocado ganhou R$:", fst, "\n","O segundo colocado ganhou R$:", scnd, "\n", "O terceiro colocado ganhou R$:", thrd)