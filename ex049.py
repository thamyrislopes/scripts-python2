#REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA, UTILIZANDO O LAÇO FOR.
n = int(input('Digite um número para ver a tabuada dele: '))
print('-' * 20)
print('A tabuada de {} é:'.format(n))
for c in range (1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
print('-' * 20)