while True:
    print()
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    op = input('Digite um operador: ')
    exit = input('Deseja sair? [s]im ou [n]ão: ')
    if exit == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Digite um numero valido')
        continue



    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == 'x':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    else:
        print('operador invalido!')