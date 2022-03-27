print('{:=^40}'.format('LOJAS GUANABARA'))
preco = float(input('Valor das compras: '))
print('FORMAS DE PAGAMENTO:\n'
      '[ 1 ] VISTA DINHEIRO/CHEQUE\n'
      '[ 2 ]  A VISTA CARTÃO\n'
      '[ 3 ] 2X NO CARTÃO\n'
      '[ 4 ] 3X OU MAIS NO CARTÃO')
opcao = int(input('QUAL É A OPÇÃO: '))

if opcao == 1:
    total = preco -(preco * 10 / 100)
elif opcao == 2:
    total = preco -(preco * 5 / 100)
elif opcao ==  3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x  de {}R$'.format(parcela))
elif opcao == 4:
    numeroParcela = int(input('Numeros de parcelas: '))
    total = preco +(preco * 20 / 100)
    parcela = total / numeroParcela
    print('Sua compra sera parcelada em {} vezes de {} R$'.format(numeroParcela,parcela))

print('Sua compra  de R${:.2f} vai custar R$ {} no final.'.format(preco,total))


