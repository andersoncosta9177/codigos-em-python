sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, Informe seu sexo: [M/F]')).upper().strip()

print('Sexo {} registrado com sucesso'.format(sexo))