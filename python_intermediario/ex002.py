n = int(input('digite um numero inteiro.'))
print('Escolha uma das bases:')
op = int(input('[1] - Binario\n'
               '[2] - octal\n'
               '[3] - hexadecimal:\n '))


if op == 1:
    print('{} convertido para binario é igual a {}'.format(n, bin(n)[2:]))
elif op ==2:
    print('{} convertido para octal é igual a {}'.format(n, oct(n)[2:]))
elif op  == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opçao invalida!')



