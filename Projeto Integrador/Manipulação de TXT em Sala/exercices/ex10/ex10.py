x = input("Digite sua senha: ")

with open("pass.txt", "r") as file:
    passw = file.read()
if x == passw:
 print("Senha correta!")
else:
 print("Senha incorreta!")