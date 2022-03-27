km = int(input('Digite a distancia da viagem!: '))
valor =  0
if  km < 200:
    valor = km * 0.50
else:
    valor = km * 0.45
print('Voçe ira pagar {} R$ de passagem!'.format(valor))

