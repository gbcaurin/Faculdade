try:
  with open("text.txt", "r", encoding="utf-8") as file:
    content = file.read()
    if content:
      print("Arquivo possui conteudo")
    else:
      print("Arquivo vazio") 
except FileNotFoundError:
  print("O arquivo não foi encontrado.")
  with open("text.txt", "w", encoding="utf-8") as file:
    file.write("Este é um arquivo de texto criado para o exercício 11.")
    print("O arquivo foi criado com sucesso.")