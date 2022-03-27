nome = input('Qual e seu nome: ')
idade = int(input('Qual e sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

nasc = 2022 - idade
imc = peso / (altura** 2)

print('================')
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Ano Nasc: {nasc}')
print(f'Imc: {imc}')