velocity = float(input('Qual a velocidade do carro: '))

if velocity > 80:
    valor_multa = (velocity - 80) * 7
    print('Voçe foi multado por exesso de velocidade.')
    print('Voçe sera multado em {} R$'.format(valor_multa))
else:
    print('Voçe na velocidade permitida.Parabens!')