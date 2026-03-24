with open("pass.txt", "r") as file:
    if file.read() == "1234":
        print("Senha correta!")
    else:
        print("Senha incorreta.")