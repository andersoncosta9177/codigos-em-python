nasc = int(input('Ano de nascimento: '))
ano_atual = 2022
idade = ano_atual  - nasc
tempoFalta = 18 - idade
passouTempo = idade - 18

print('Sua idade é {} anos'.format(idade))
if idade == 18:
    print('Esta na hora de fazer seu alistamento militar')
elif idade  > 18:
    print('Voçe ja passou da idade de se alistar.')
    print('Voçe devia ter se alistado ha {} anos atras.'.format(passouTempo))
else:

    print('Ainda nao chegou a data para voçe se alistar.')
    print('Faltam {} anos'.format(tempoFalta))