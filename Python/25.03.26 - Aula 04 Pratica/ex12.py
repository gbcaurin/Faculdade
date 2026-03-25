n = int(input("Digite um numero inteiro e descubra se ele é primo: "))
i = 0

if n <= 1:
  print("Nunca sera")
elif n  == 2:
  print("Eh primo demais")
else:
 for c in range(2, n):
   if n % c == 0:
     i += 1
 if i == 0:
  print("Eh primo demais")
 else:
  print("Nunca sera")