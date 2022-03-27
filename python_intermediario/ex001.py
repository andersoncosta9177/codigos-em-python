casa = float(input('Valor da casa R$: '))
salario = float(input('Salario: '))
anos = int(input('Anos de financiamento: '))
minimo = salario * 30 / 100
prestacao = casa / (anos * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos.'.format(casa,anos))
print('A prestaçao sera de R$ {}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo pode ser aceito.')
else:
    print('Emprestimo negado.')




