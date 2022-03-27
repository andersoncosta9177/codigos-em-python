phase = str(input('Digite uma frase: ')).strip().upper()
words = phase.split()
words_together = ''.join(words)
inverse = ''
for word in range(len(words_together) - 1, -1, -1):
    inverse += words_together[word]
if words_together == inverse:
    print('Esta frase é um palindrome.')
else:
    print('Frase não é um palindrome.')
