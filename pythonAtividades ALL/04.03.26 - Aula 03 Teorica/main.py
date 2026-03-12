#adiantando provavelmente uma atividade futura, ler um numero inteiro de tres digitos e retornar o numero invertido  da Aula pratica 02
num = int(input("Digite um numero inteiro: "))
num1 = num // 100
num2 = (num % 100) // 10
num3 = num % 10
inv = (num3 * 100) + (num2 * 10) + num1
print(f"{num} invertido é: {inv}")