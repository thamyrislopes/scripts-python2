print('{:=^40}'.format(' LOJAS LOPES '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preço - (preço * 10 / 100)
elif opcao == 2:
    total = preço - (preço * 5 / 100)
elif opcao == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))

"""^ : centralizado"""

"""print('='*15, end='')
print(' LOJAS LOPES ', end='')
print('='*15)
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    desconto = preço * (10 / 100)
    valor = preço - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, valor))
elif opcao == 2:
    desconto = preço * (5 / 100)
    valor = preço - desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, valor))
elif opcao == 3:
    parcela = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
    print('Sua compra vai custar R${:.2f} no final.'.format(preço))
elif opcao == 4:
    escolha = int(input('Quantas parcelas? '))
    juros = (preço * 20/100) / escolha
    parcela = (preço / escolha) + juros
    valor = escolha * parcela
    print('Sua compra será parcelada em {}x de {}  COM JUROS.'.format(escolha, parcela))
    print('Sua compra de R${} vai custar {} no final.'.format(preço, valor))
else:
    print('Escolha uma opção válida')"""
