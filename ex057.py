#Faça um programa que leia o sexo, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

'''s = 'F'
while s == 'F' or s == 'M':
    s = str(input('O sexo é feminino ou masculino? Escolha uma das opções [F/M]: ')).upper()
print('Escolha uma opção válida!')'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper() [0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))