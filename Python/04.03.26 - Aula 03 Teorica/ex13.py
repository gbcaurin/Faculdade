#Ler um numero inteiro de ate dois digitos e retornar a soma de ambos
num = int(input("Digite um numero inteiro de até dois dígitos: "))
num1 = num // 10
num2 = num % 10
soma = num1 + num2
print(f"A soma dos dígitos de {num} é: {soma}")