#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont = 0
n = int(input('Digite um número: '))
for c in range (1, n + 1):
    if n % c == 0:
        cont += 1
        print('\033[1;36m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, cont))
if cont > 1 and cont <= 2:
    print('Por isso, ele É PRIMO.')
else:
    print('Por isso, ele NÃO É PRIMO.')

