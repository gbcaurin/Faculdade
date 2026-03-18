'''
Fazer um programa para resolver uma equação do 1º grau com duas variáveis, ou seja, uma equação da forma Ax + By = C, onde A, B e C são coeficientes 
fornecidos pelo usuário. O programa deve solicitar os valores de A, B e C, e então calcular e exibir as soluções para x e y. Se a equação não tiver
soluções, o programa deve informar ao usuário.

criar input com map facilita a entrada de dados, o usuario pode digitar os 6 coeficientes separados por espaço, e o programa irá atribuir cada valor à
variável correspondente (A, B, C, D, E, F).

O programa então verifica se a equação tem soluções reais e calcula as soluções para x e y usando a fórmula de resolução de sistemas lineares. Se a equação
não tiver soluções, o programa informa ao usuário.
'''


a, b, c, d, e, f = map(int, input("Digite os coeficientes da equação (A, B, C, D, E, F): ").split())
if (a * e) - (b * d) != 0:
    x = ((c * e) - (b * f)) / ((a * e) - (b * d))
    y = ((a * f) - (c * d)) / ((a * e) - (b * d))
    print(f"As soluções da equação são: x = {x:.2f} e y = {y:.2f}.")
else:
    print("A equação não possui soluções.")