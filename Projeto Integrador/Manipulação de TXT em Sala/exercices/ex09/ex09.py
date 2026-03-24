x =   int(input("Digite um numero inteiro: "))

with open("num09.txt", "w") as file:
    file.write(f"{x}")

with open("num09.txt", "r") as file:
    content = file.read()
    if content > "10":
      print("O número é maior que 10.")
      print(f"O valor lido é: {content}")
    else:
      print("O número é menor ou igual a 10.")
      print(f"O valor lido é: {content}")
