#ignorando o 5 e indo fazer o DESAFIO

x = input("Digite uma palavra para descobrir se ela eh palindroma: ")

txt = x.lower().replace(" ", "")#tirando os espacos e deixando tudo minusculo para comparar melhor

if txt == txt[::-1]:
    print(f'"{x}" eh palindroma.')
else:
    print(f'"{x}" nao eh palindroma.')


#escrevendo qualquer coisa para ver se meu copilot vai entrosar
#teste de escrita
#teste de entrosa do copilot