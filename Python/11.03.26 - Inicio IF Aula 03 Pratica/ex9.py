#Ler a idade de lutador, se for menor que 18, Categ juvenil. Se for maior de 18 e com peso menor que 80, Peso Médio. Se for maior de 18 e peso maior que 80
#Peso Pesado.   
age = int(input("Digite sua idade: "))
if age < 18:
  print("Categoria Juvenil")
else:
  peso = int(input("Digite seu peso em KGs: "))
  if peso <= 80:
    print("Peso Médio")
  else:
    print("Peso Pesado")