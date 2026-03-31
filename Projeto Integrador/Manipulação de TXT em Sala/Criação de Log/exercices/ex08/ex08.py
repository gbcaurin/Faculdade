try:
  with open("dadosex08.txt", "r") as file:
    cont = file.read()
    print(cont)
except FileNotFoundError:
  print("O arquivo não existe")
  with open("dadosex08.txt", "w") as file:
    file.write("Arquivo criado. Arquivo: dadosex08.txt")