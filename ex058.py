#Melhore o jogo do DESAFIO 028, no qual o computador vai "pensar" em um número entre 0 e 10. Só que agora, o jogador vai tentar adivinhar até acertar, mostrando no final, quantos palpites foram necessários para vencer.
'''from random import randint
from time import sleep 
print ('-=-' * 21)
print('Vou mostrar um número entre 0 e 10. Será que você vai acertar?')
print('-=-' * 21)
computador = randint(0, 10)
jogador = 0
c = 0
while jogador != computador:
    computador = randint(0, 10)
    jogador = int(input('Qual foi o número escolhido? '))
    print('PROCESSANDO...')
    sleep(0.5)
    if jogador != computador: 
        print('Eu ganhei! Eu escolhi {} e você {}. Tente descobrir qual o número que irei escolher...'.format(computador, jogador))
    c += 1
print('PARABÉNS! Você venceu! Eu escolhi {} e você {}.'.format(computador, jogador))
print('Você tentou {} vezes até vencer.'.format(c))'''

from random import randint
computador = randint(0, 10)
print('Sou o seu computador... Você consegue acertar o número que "pensei"?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('O número é maior... Tente outra vez.')
        elif jogador > computador:
            print('O número é menor... Tente outra vez.')
print('Acertou com {} palpites!'.format(palpites))