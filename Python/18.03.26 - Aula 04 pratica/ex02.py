while True:
  n1 = int(input("Digite um número: "))
  n2 = int(input("Digite outro número: "))
  print(f"Os numeros digitados foram: {n1} e {n2}")
  n3 = int(input("Digite outro numero: "))
  if n3 > n1 and n3 < n2:
    print(f"O número {n3} está entre {n1} e {n2}.")
  else:
    print(f"O número {n3} não está entre {n1} e {n2}.")