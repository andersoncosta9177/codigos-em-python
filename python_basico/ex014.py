dias = int(input('Dias alugados: '))
km = int(input('km rodados: '))
preco_dia = float(input('Valor diario: '))
valor_km = float(input('Valor por km: '))


total_pagar_diarias = dias * preco_dia
total_pagar_km = km * valor_km
total_pagar = total_pagar_diarias + total_pagar_km

print('voçe ficou com o carro por {} dias, ira pagar {} reais.'.format(dias, total_pagar_diarias))
print('Voçe andou {} km com o carro, o valor por km é {}, valor a pagar: {}'.format(km, valor_km,total_pagar_km))
print('O valor total da compra sera de {} reais.'.format(total_pagar))