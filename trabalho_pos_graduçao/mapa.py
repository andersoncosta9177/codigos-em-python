listas = [[]]

while True:
    print("1-Cadastrar pessoa: ")
    print("2-Alterar dados da pessoa: ")
    print("3-Listar dados da pessoa: ")
    print("4-Pesquisar dados da pessoa: ")
    print("5-Excluir dados da pessoa: ")
    print("6-Sair do sistema: ")

    op = int(input())
    if op == 1:
        nova = [] # cria uma lista para adicionar o id, nome e idade da pessoa
        id = int(input('Id da pessoa: '))
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        cidade = input("Cidade: ")
        estado = input('Estado: ')


        nova.append(id)
        nova.append(nome)
        nova.append(telefone)
        nova.append(cidade)
        nova.append(estado)
        nova.append(status)

        listas.append(nova)


   # if op == 2: # alterar dados da pessoa





    elif op == 3:    # MOSTRA OS DADOS DA PESSOA
        for mostrar in listas:
            for mostrar2 in mostrar:
                print(mostrar)#mostra tudo dentro da









    elif op == 6:
        print("Programa encerrado.")
        break





