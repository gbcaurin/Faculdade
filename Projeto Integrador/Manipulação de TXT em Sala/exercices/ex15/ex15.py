x = input("Digite seu nome: ")

if x == "":
    print("Nome invalido. Por favor, digite um nome.")
else:
    with open("name.txt", "a", encoding="utf-8") as file:
        file.write(f"{x}\n")

