from conection import create_user, edit_user, delete_user, list_users

print("\n 1 - Criar usuário \n 2 - Editar usuário \n 3 - Deletar usuário \n 4 - Listar usuários \n")
Q = int(input("\n Digite o numero da operação que deseja realizar:"))

if Q == 1:
    name = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    password = input("Digite a senha do usuário: ")
    create_user(name, email, password)
elif Q == 2:
    id = input("Digite o ID do usuário a ser editado: ")
    name = input("Digite o novo nome do usuário: ")
    email = input("Digite o novo email do usuário: ")
    password = input("Digite a nova senha do usuário: ")
    edit_user(id, name, email, password)
elif Q == 3:
    id = input("Digite o ID do usuário a ser deletado: ")
    delete_user(id)
elif Q == 4:
    list_users()
else:   
    print("Opção inválida!")
 
