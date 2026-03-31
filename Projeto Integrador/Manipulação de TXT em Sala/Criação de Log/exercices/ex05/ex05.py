x = input("Digite uma palavra: ")
z = input("Voce deseja salvar esta palavra? (s/n) ")

if z == "s":
    with open("palavras.txt", "a") as file:
        file.write(f"{x}\n")
    print("Palavra salva com sucesso!")
elif z == "n":
    print("Palavra não salva.")
else:
    print("Opção inválida. Por favor, responda com 's' ou 'n'.")