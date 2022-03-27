salario = float(input('Salario do funcionario: '))
aumento = float(input('Digite o valor do aumento:'))

totalAumento = salario * aumento / 100
totalSalario = salario + (salario * aumento /100)

print('O total do aumento foi de {:.2f}%'.format(totalAumento))
print('O novo salario sera de {:.2f}'.format(totalSalario))