nome_arq = "ex04.txt"
try:
  with open(nome_arq, "r", encoding="utf-8") as arq:
    content = arq.read()
    print(content)
except FileNotFoundError:
  print("Arquivo não encontrado.")
  with open(nome_arq, "w", encoding="utf-8") as arq:
    arq.write("Arquivo criado.")