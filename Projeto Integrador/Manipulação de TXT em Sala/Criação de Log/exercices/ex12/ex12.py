x = int(input("Digite sua idade: "))

with open("ex12.txt", "a", encoding="utf-8") as file:
    if x < 18:
        print("Você é menor de idade. Desculpe, mas você não pode entrar.")
    else:
        file.write(f"{x}\n")
        print("Você é maior de idade. Bem-vindo!")