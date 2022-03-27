salario = float(input('Digite o salario do funcionario: '))

novosalario = 0

if salario > 1250:
    novosalario = salario + (salario * 10 / 100)
else:
    novosalario = salario +(salario * 15 /100)

print('Seu novo salario é de {} R$.'.format(novosalario))
