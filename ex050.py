#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
q = 0
for c in range (1 , 7):
    n = int(input('Digite o {}º valor inteiro: '.format(c)))
    if n % 2 == 0:
        s += n
        q += 1
print('Você informou {} número(s) par(es) e a soma é: {}'.format(q, s))