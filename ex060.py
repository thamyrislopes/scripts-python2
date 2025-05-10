'''Faça um programa que leia um número qualquer e mostre o fatorial dele.

Ex: 5! = 5x4x3x2x1 = 120'''
c = 1
n = 2 
m = n - 1
n = int(input('Digite um número inteiro: '))
print('{}! = '.format(n), end='')
while n > 0:
    if n != 0:
        print('{}x'.format(n), end='')
        m = m * n
        n -= c
print(' = {}'.format(m))
    
    