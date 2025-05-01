#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMERO ÍMPARES QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma dos {} valores é {}.'.format(cont, soma))