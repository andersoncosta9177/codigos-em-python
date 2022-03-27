def exibir_menu():
    print('''Escolha uma opção:

    1. Cadastrar uma pessoa
    2. Alterar dados da pessoa
    3. Listar pessoas cadastradas
    4. Procurar dados de uma pessoa
    5. Excluir dados da pessoa
    6. Sair do sistema.
    ''')

def cadastrar(pessoas):
    identificador = input('Id? ')
    nome = input('Nome? ')
    telefone = input('Telefone?')
    cidade = input('Cidade? ')
    estado = input('Estado?')
    status = input('(P-> Pessoal) ou (C-> Comercial): ')
    pessoas.append((identificador, nome, telefone, cidade, estado, status))

def alterar(pessoas):

    identificador_desejado = input('Id? ')
    for pessoa in pessoas:
        identificador, nome, telefone, cidade, estado, status  = pessoa
        dadosAlterados = []
        if identificador == identificador_desejado:
            identificador = input('Id? ')
            nome = input('Nome? ')
            telefone = input('Telefone?')
            cidade = input('Cidade? ')
            estado = input('Estado?')
            status = input('(P-> Pessoal) ou (C-> Comercial): ')
            dadosAlterados.append((identificador,nome,telefone,cidade,estado, status))
            pessoas.append((identificador, nome, telefone, cidade, estado, status))

            break
    else:
        print(f'Pessoa com id {identificador_desejado} não encontrada')

def excluir(pessoas):
    identificador_desejado = input('Id? ')
    for pessoa in pessoas:
        identificador, nome, telefone, cidade, estado, status = pessoa
        if identificador == identificador_desejado:
            pessoas.clear()
            print('Pessoa removida com sucesso!')

            break
    else:
        print(f'Pessoa com id {identificador_desejado} não encontrada')

def listar(pessoas):
    for pessoa in pessoas:
        identificador, nome, telefone, cidade, estado,status   = pessoa
        print(f'Nome: {nome}, Telefone: {telefone}, Cidade:{cidade}, Estado: {estado}, Status: {status} id: {identificador}')

def buscar(pessoas):
    identificador_desejado = input('Id? ')
    for pessoa in pessoas:
        identificador, nome, telefone, cidade, estado, status  = pessoa
        if identificador == identificador_desejado:
            print(f'Nome: {nome}, Telefone: {telefone}, Cidade: {cidade}, Estado: {estado}, Status: {status}, id: {identificador}')
            break
    else:
        print(f'Pessoa com id {identificador_desejado} não encontrada')

def main():
    pessoas = []

    while True:
        exibir_menu()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(pessoas)
        elif opcao == 2:
            alterar(pessoas)
        elif opcao == 5:
            excluir(pessoas)
        elif opcao == 3:
            listar(pessoas)
        elif opcao == 4:
            buscar(pessoas)

        elif opcao == 6:
            print('Sistema encerrado.')
            break
        else:
            print('Opção inválida')


main()