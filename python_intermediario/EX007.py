peso = float(input('Qual e seu peso:'))
altura = float(input('Qual e sua altura: '))
imc = peso / (altura ** 2)

print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Voçe esta abaixo do peso.')
elif imc < 24.9:
    print('Voçe esta no peso normal.')
elif imc < 29.9:
    print('Voçe esta com sobrepeso.')
elif imc < 34.9:
    print('Voçe esta com obesidade grau 1')
elif imc < 39.9:
    print('Voçe esta com obesidade grau 2')
elif imc >= 40:
    print('Voçe esta com obesidade grau 3 ou Morbida')
else:
    print('Dados incorretos.')
