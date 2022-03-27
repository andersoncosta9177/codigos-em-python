num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um numero: [999 para parar: ]'))
    cont += 1
    soma += num

print('Voçe digitou {} numeros'.format(cont - 1))
print('E a soma total foi de {}'.format(soma - 999))
