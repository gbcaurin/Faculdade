with open("num.txt", "r") as file:
    content = int(file.read())
    if content % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")