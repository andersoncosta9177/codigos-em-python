nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda  nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Voçe esta aprovado')
elif media > 5 and media <= 6.9:
    print('Voçe esta de recuperaçao')
else:
    print('Voçe esta reprovado')

