#Caixa de uma loja.
valor = int(input("Digite o valor da sua compra:"))
pay = int(input("Digite quando voce ira dar em dinheiro:"))
troco = pay - valor

#aqui poderia ter colocado troco %= 100, mas preferi fazer o processo passo a passo para entender melhor
c_100 = troco // 100                      
troco = troco % 100
c_50 = troco // 50
troco = troco % 50
c_20 = troco // 20
troco = troco % 20
c_10 = troco // 10
troco = troco % 10
c_5 = troco // 5
troco = troco % 5
c_1 = troco //1
troco = troco % 1
print(c_100, "cedula(s) de R$100\n",
        c_50, "cedula(s) de R$50\n",
          c_20, "cedula(s) de R$20\n",
            c_10, "cedula(s) de R$10\n",
              c_5, "cedula(s) de R$5\n",
                c_1, "cedula(s) de R$1\n",
                  "Total do troco: R$", pay - valor)