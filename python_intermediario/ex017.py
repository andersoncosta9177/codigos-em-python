from  datetime import  date
atual = date.today().year
totalmaior =  0
totalmenor =0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        print('Essa pessoa é de maior')
        totalmaior += 1
    else:
        print('Essa pessoa ainda nao e de maior')
        totalmenor +=1
print('{} pessoas maiores de idade'.format(totalmaior))
print('{} pessoas menores de idade'.format(totalmenor))

