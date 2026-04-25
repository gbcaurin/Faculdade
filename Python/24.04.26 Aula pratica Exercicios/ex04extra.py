A = [1, 2, 8, [5, 6, 7], 19, [2, [3, 4, 7]], 8]

#determinar A[3][1] que eh 6, Explicacao: A[3] eh a lista de [5, 6, 7] e A[3][1] eh o 7 (lembrando que a primeira posicao da lista eh a 0)

#determinar len(A[5][1]) que eh 3, Explicacao: A[5] eh a lista de [2, [3, 4, 7]] e A[5][1] eh a lista de [3, 4, 7], entao len(A[5][1]) eh o tamanho da lista de [3, 4, 7] que tem 3 elementos

#determinar A[5][1][2] que eh 7, Explicacao: A[5] eh a lista de [2, [3, 4, 7]] e A[5][1] eh a lista de [3, 4, 7], entao A[5][1][2] eh o elemento da lista de [3, 4, 7] que esta na posicao 2 (lembrando que a primeira posicao da lista eh a 0) que eh o numero 7

#construir uma lista com os valores de A[5][1]

#construir um prgrama que leia quantos pares tem na lista..

lista = A[5][1]
print("Lista de A[5][1]:", lista)

pares = []
for i in A:
    if type(i) == list:
        for j in i:
            if type(j) == list:
                for k in j:
                    if k % 2 == 0:
                        pares.append(k)
            elif j % 2 == 0:
                pares.append(j)
    elif i % 2 == 0:
        pares.append(i)

print(f"Quantidade de números pares: {len(pares)}")