x = input("Digite uma palavra: ")

with open("palavra.txt", "a") as file:
    file.write(f"{x}\n")