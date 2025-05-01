from datetime import date
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('Quem nasceu em {}, vai fazer ou está com {} anos em {}.'.format(nasc, idade, ano))
if idade < 18:
    dif = 18 - idade
    dif2 = dif + ano
    print('Ainda faltam {} anos para o alistamento.'.format(dif))
    print('O seu alistamento será em {}.'.format(dif2))
elif idade == 18:
    dif = 18 - idade
    print('Você tem que se alistar IMEDIATAMENTE!'.format(dif))
elif idade > 18:
    dif = idade - 18
    dif2 = ano - dif
    print('Você já deveria ter se alistado há {} anos.'.format(dif))
    print('O seu alistamento foi em {}.'.format(dif2))