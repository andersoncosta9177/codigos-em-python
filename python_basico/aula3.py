usuario = input('Digite seu usuario: ')
senha = input('Digite sua senha: ')

usuario_bd = 'ander'
senha_bd = '1234'

if usuario_bd == usuario and senha_bd == senha:
    print('Usuario logado com sucesso!')
else:
    print('Dados incorretos! Tente novamente!')