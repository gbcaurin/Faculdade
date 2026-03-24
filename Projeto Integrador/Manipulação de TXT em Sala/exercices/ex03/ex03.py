x = int(input("Digite sua idade: "))

if x >= 18:
    print("Você é maior de idade.")
    with open("age.txt", "a") as file:
        file.write(f"{x}\n")
else:
    print("Você não é maior de idade.")