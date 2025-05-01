# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
#pegar a data atual:
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = ano - nasc
    if idade > 18:
        maior += 1
    else: 
        menor += 1
print('Menores de idade: {}, Maiores de idade: {}'.format(menor, maior))

