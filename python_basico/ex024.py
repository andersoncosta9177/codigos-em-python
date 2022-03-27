from random import  randint
from time import  sleep
computador = randint(0,5)
humano = int(input('Digite um numero: '))
print('Processando.....')
sleep(2)
print('Eu escolhi o numero: {}'.format(computador))
print('E voçe escolheu o numero {} '.format(humano))
if computador == humano:
    print('Parabens!! voçe acertou!')
else:
    print('Voçe errou!, Tente novamente')