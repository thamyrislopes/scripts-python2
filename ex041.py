from datetime import date
ano = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 8:
    print('Classificação: PRÉ-MIRIM.')
elif 10 >= idade:
    print('Classificação: MIRIM.')
elif 12 >= idade:
    print('Classificação: PETIZ.')
elif 16 >= idade:
    print('Classificação: INFANTO-JUVENIL.')
elif 19 >= idade:
    print('Classificação: JUNIOR.')
elif idade >= 20:
    print('Classificação: SÊNIOR.')