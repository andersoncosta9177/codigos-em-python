soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma total dos numeros multiplos de 3 foi: {} '.format(soma))
print('Quantidade de numeros: {} '.format(cont))

