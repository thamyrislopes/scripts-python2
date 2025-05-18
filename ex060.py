'''Faça um programa que leia um número qualquer e mostre o fatorial dele.

Ex: 5! = 5x4x3x2x1 = 120'''

'''c = 1
n = 2 
m = n - 1
n = int(input('Digite um número inteiro: '))
print('{}! = '.format(n), end='')
while n > 0:
    print('{}'.format(n), end='')
    if n != 0:
        print('x', end='')
        m = m * n
        n -= c
print(' = {}'.format(m))'''

'''from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print('{}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
    
    