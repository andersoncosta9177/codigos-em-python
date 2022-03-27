n1 =int(input('Primeiro Numero: '))
n2 = int(input('Segundo numero: '))
opcao = 0
total = 0

while opcao != 5:
    print('''[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros: 
    [ 5 ] sair do programa. ''')
    opcao = int(input('SUA OPÇAO: '))

    if opcao == 1:
        total = n1 + n2
        print('{} + {} = {}'.format(n1,n2,total))

    elif opcao == 2:
        total = n1 * n2
        print('{}  x {} = {}'.format(n1,n2,total))


    elif opcao == 3:
        if n1 == n2:
            print('Os numeros sao iguais!')
        else:
            maior = max(n1, n2)
            print('O numero {} é maior'.format(maior))


    elif  opcao == 4:
        n1 = int(input('Primeiro Numero: '))
        n2 = int(input('Segundo numero: '))

    else:
        print('Opcao invalida!')




print('Fim do programa.')

