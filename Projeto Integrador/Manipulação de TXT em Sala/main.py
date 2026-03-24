#Manipulação de Arquivo .txt com Python

#(w) para escrever e sobrescrever, (a) para escrever um em cima do outro
#with open("arq.txt", "a", encoding="utf-8") as arq: #cria o arquivo. (se estiver dentro da pasta certa, entrar com cdno terminal)
    #arq.write("Testado\n") #coloca escrita no arquivo

#ler um arquivo
#with open("arq.txt", "r", encoding="utf-8") as arq:
    #content = arq.read()
    #print(content)

#ler arquivo inexistente com try catch
nome_arq = "arq1.txt"
try:
  with open(nome_arq, "r", encoding="utf-8") as arq:
    content = arq.read()
    print(content)
except FileNotFoundError:
  print("Arquivo não encontrado.")
  with open(nome_arq, "w", encoding="utf-8") as arq:
    arq.write("Arquivo criado. Arquivo: " + nome_arq)

#top