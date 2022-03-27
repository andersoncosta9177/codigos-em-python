frase = 'o rato roeu a roupa do rei'
tamanha_frase = len(frase)
contador = 0
novaString = ''

while contador < len(frase):
    letra = frase[contador]
    if letra == 'r':
        novaString += 'R'
    else:
        novaString += letra
    contador += 1
print(novaString)