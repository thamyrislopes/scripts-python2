'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão, usando a estrutura 'while'''

print('='*30)
print('10 TERMOS DE UMA P.A.'.center(30))
print('='*30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + 10 * razão
while primeiro != décimo:
    print('{}'.format(primeiro), end=' → ')
    primeiro += razão
print('FIM.')
