
import  random
n1 = input('primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Tereiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1,n2,n3,n4]

escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
