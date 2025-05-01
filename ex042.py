n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2: 
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO.')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')

"""n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
triangulo = n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2
if  triangulo and n1 != n2 and n1 != n3 and n2 != n3:
    print ('Os segmentos acima PODEM FORMAR um triângulo ESCALENO.')
elif triangulo and n1 == n2 and n1 != n3 or n1 == n3 and n1 != n2 or n2 == n3 and n2 != n1:
    print ('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES.')
elif triangulo and n1 == n2 and n1 == n3 and n2 == n3:
    print ('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')"""