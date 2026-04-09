def itens(x):
  ppa = 2
  ppo = 1.5
  parr = 0.75

  if x == "Parafuso":
    y = int(input("Digite a quantidade: "))
    valpa = y * ppa
    print(f"O valor total é: R$ {valpa:.2f}")

  elif x == "Porcas":
    y = int(input("Digite a quantidade: "))
    valpo = y * ppo
    print(f"O valor total é: R$ {valpo:.2f}")

  elif x == "Arruelas":
    y = int(input("Digite a quantidade: "))
    valar = y * parr
    print(f"O valor total é: R$ {valar:.2f}")

  else:
    print("Opção inválida.")

x = input("Digite o que deseja comprar: Parafuso/Porcas/Arruelas ")
itens(x)