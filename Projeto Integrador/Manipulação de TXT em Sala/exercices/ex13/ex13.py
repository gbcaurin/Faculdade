x = input("Voce deseja limpar o conteudo do arquivo? (s/n): ")

if x == "s":
  with open("data.txt", "w") as file:
    file.write("")
  print("Conteudo do arquivo limpo.")
elif x == "n":
  print("Conteudo do arquivo mantido.")
else:
  print("Entrada invalida. Por favor, responda com 's' ou 'n'.")
