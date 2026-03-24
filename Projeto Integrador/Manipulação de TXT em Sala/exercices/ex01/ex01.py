x = input("Digite seu nome: ")

with open("ex01.txt", "w", encoding="utf-8") as arq:
    arq.write(x)