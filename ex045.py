from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!!')
print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador ==1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador ==1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

"""from random import randint
from time import sleep
computador = randint (1, 3)
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL 
[ 3 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-='*15)
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(jogador))
print('-='*15)
if jogador == 2 and computador == 3:
    print('JOGADOR PERDE')
elif jogador == 1 and computador == 2:
    print('JOGADOR PERDE')
elif jogador == 1 and  computador == 3:
    print('JOGADOR VENCE')
elif jogador == 3 and computador == 2:
    print('JOGADOR VENCE')
elif jogador == 2 and computador == 1:
    print('JOGADOR VENCE')
elif jogador == computador:
    print('EMPATE')
else:
    print('Digite uma opção válida!')"""
