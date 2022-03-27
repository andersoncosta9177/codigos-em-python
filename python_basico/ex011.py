preco = float(input('Digite o preço do produto: '))
desconto = int(input('Digite o valor do desconto: '))

total_desconto = preco * desconto /100
novopreco =  preco - (preco * desconto / 100)

print('O desconto foi de {} reais'.format(total_desconto))
print('O novo valor é {}'.format(novopreco))
