from random import  shuffle

n1 = input('Primeiro nome: ')
n2 = input('Segundo  nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1,n2,n3,n4]
shuffle(lista)
print(lista)