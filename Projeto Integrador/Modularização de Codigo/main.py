import operations

option = 0

while option != 5:
  print("Calculadora")
  print("1 - Adição")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")
  print("5 - Sair")

  option = int(input("Escolha uma opção: "))
  
  match option: 
    case 1:
        print("Opção selecionada: Adição")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        result = operations.add(n1, n2)
        print(f"Resultado: {result}")

        with open("calc.txt", "a", encoding="utf-8") as f:
            f.write(str(n1) + " + " + str(n2) + " = " + str(result) + "\n")
            

    case 2:
        print("Opção selecionada: Subtração")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        result = operations.subtract(n1, n2)
        print(f"Resultado: {result}")

        with open("calc.txt", "a", encoding="utf-8") as f:
            f.write(str(n1) + " - " + str(n2) + " = " + str(result) + "\n")

    case 3:
        print("Opção selecionada: Multiplicação")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        result = operations.multiply(n1, n2)
        print(f"Resultado: {result}")

        with open("calc.txt", "a", encoding="utf-8") as f:
            f.write(str(n1) + " * " + str(n2) + " = " + str(result) + "\n")

    case 4:
        print("Opção selecionada: Divisão")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        result = operations.divide(n1, n2)
          
        if result == None:
            print("Erro: Divisão por zero não é permitida.")
        else:
            print(f"Resultado: {result}")

            with open("calc.txt", "a", encoding="utf-8") as f:
                f.write(str(n1) + " / " + str(n2) + " = " + str(result) + "\n")

    case 5:
        print("Saindo...")

    case _: #acontece se for digitado um numero diferente de 1 a 5.
        print("Erro: Opção inválida")