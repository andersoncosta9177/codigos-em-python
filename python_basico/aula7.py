#l2 = ['string',True, 10, -30.5]

#for elem in l2:
   # print(f'O tipo de {elem} é {type(elem)}')
secreto = 'mal'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Voçe perdeu todas as suas chances!')
        break
    letra = input('Digite uma letra: ')

    if len(letra) >1:
        print('Ahhh! isso nao vale, digite apenas uma letra!')
        continue
    digitadas.append(letra)


    if letra in secreto:
       print(f'UHUULLL, a letra "{letra}" existe na palavra secreta')
    else:
       print(f'Affzz: a letra "{letra}" nao existe na palavra secreta')
       digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, voçe ganhou, a palavra secreta era: {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')
    if letra not in secreto:
        chances -= 1

        print(f'Voçe ainda tem {chances} chances.')
        print()



