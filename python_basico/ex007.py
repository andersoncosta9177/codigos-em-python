nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) /2
print('A media do aluno foi {}'.format(media))
if media >= 7:
    print('Aprovado')
else:
    print('Reprovado.')
