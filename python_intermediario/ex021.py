from random import  randint
computador  = randint(0, 10)

print('Sou seu computador... Acabei de pensar em um numero emtre 0 e 10')
print('Sera que voçe consegue adivinhar qual foi?')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('E um numero maior!')
        else:
            print('E um numero menor!')


print('Acertou com {} palpites'.format(palpites))

