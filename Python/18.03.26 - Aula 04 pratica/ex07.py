 
cod = int(input("Digite o código para descobrir o produto: "))

if cod == 1:
  print("Alimento não perecivel")
if cod >=2 and cod <=4:
   print("Alimento perecivel")
if cod == 5 or cod == 6:
   print("Vestuario")
if cod == 7:
   print("Higiene Pessoal")
if cod >= 8 and cod <= 15:
   print("Limpeza e utnsilios Domesticos")
if cod > 15:
   print("INVALIDO")