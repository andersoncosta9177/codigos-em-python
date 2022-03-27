resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'sS':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('Voçe digitou {} numeros e a media foi {:.2f}'.format(quant, media))
print('E o menor numero digitado foi: {}'.format(menor))
print('E o maior numero digitado foi: {}'.format(maior))