from random import  randint
from time import  sleep
itens = ['pedra','papel','tesoura']
computador = randint(0,2)
print('Suas opcoes:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')
jogador = int(input('Qual e sua jogada?: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('=============================================')
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('================================================')

if computador == 0:  #pedra
    if jogador ==0:
        print('Empatou!')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador vence!')
    else:
        print('Jogada invalida.')

elif computador == 1: #papel
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empatou')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Jogada invalida.')
elif computador == 2: #tesoura
    if jogador == 0:
     print('Jogador venceu!')
    elif jogador == 1:
     print('Computador venceu!')
    elif jogador == 2:
     print('Empatou!')
    else:
        print('Jogada invalida.')

