#receber um numero inteiro e retornar em horas, minutos e segundos  
num = int(input("Digite um numero inteiro: "))
horas = num // 3600
minutos = (num % 3600) // 60
segundos = num % 60
print(f"{num} segundos equivalem a {horas} horas, {minutos} minutos e {segundos} segundos.")