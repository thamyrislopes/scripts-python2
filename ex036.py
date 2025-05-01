casa = float(input('Valor da casa: R$\033[1;32m'))
salario = float(input('\033[mSalário do comprador: R$\033[1;32m'))
anos = int(input('\033[mQuantos anos de financiamento? \033[1;32m'))
parcela = casa / (anos * 12)
print('\033[mPara pagar uma casa de R${:.2f} em {} anos,'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}.'.format(parcela))
if parcela > 0.3 * salario:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')