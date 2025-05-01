#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
sidade = 0
media = 0
midadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    sidade += idade
    if p == 1 and sexo in 'Mm':
    # 'Mm': para aceitar tanto maiúsculo quanto minúsculo.
        midadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > midadehomem:
        midadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = sidade / 4
print('A média de idade do grupo é de {:.2f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(midadehomem, nomevelho))
print('Ao todo, são {} mulheres com menos de 20 anos.'.format(totmulher20))
