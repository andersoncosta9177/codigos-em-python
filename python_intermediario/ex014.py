numpar = 0
numImpar = 0
for c in range(1,7):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
         numpar += n
    elif n % 2 == 1:
         numImpar += n

print('A soma total dos numeros pares é de: {}'.format(numpar))
print('A soma total dos numeros impares é de: {}'.format(numImpar))

