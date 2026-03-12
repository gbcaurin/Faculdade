#Leia um numero inteiro e imprima resultado da diferença do seu triplo pelo dobro do seu sucessor.
num = int(input("Digite um numero inteiro:"))
trip = num * 3
dobr = (num + 1) * 2
dif = trip - dobr
print("A diferença é:", dif)