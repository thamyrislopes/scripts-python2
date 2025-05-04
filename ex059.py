'''Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
op = 1
s = 0
m = 0
while op != 5:
    n1 = int(input('Digite o 1º valor: '))
    n2 = int(input('Digite o 2º valor: '))
    print('''Escolha uma das opções abaixo:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    op = int(input('Sua opção: '))
    if op == 1:
        s = n1 + n2
        print('O resultado da soma entre {} e {} é {}.'.format(n1, n2, s))
    if op == 2:
        m = n1 * n2
        print('O resultado da multiplicação entre {} e {} é {}.'.format(n1, n2, m))
    if op == 3:
        if n1 > n2:
            print('O {} é maior do que {}.'.format(n1, n2))
        else:
            print('O {} é maior do que {}.'.format(n2, n1))
    if op > 5:
        print('Digite uma opção válida!')
print('Fim!')
    