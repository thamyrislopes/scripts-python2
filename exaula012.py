nome = str(input('Qual é o seu nome? '))
if nome == 'Thamyris':
    print('Que nome bonito!')
elif nome == 'José' or nome == 'Maria' or nome == 'João':
    print('O seu nome é popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('É um nome feminino.')
else:
    print('Seu nome é ok!')
print('Tenha um bom dia, {}!'.format(nome))