#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

'''print('='*30)
print('10 TERMOS DE UMA P.A. '.center(30))
print('='*30)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range (10):
    print(t, end=' → ')
    t += r
print('FIM')'''

print('='*30)
print('10 TERMOS DE UMA P.A.'.center(30))
print('='*30)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' → ')
print('FIM.')