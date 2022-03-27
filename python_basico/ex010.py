largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura * altura
tinta = area / 2

print('A parede em mede {} metros quadrados'.format(area))
print('Voçe ira usar {} litros de tinta para pintar'.format(tinta))