'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

print('='*30)
print('10 TERMOS DE UMA P.A.'.center(30))
print('='*30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + 10 * razão
resposta = 'Ss'
while primeiro != décimo and resposta == 'Ss':
    print('{}'.format(primeiro), end=' → ')
    primeiro += razão
print(end='\n')

