numero = int(input('Digite um número inteiro: \033[1;32m'))
print('''\033[mEscolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: \033[1;32m'))
if opcao == 1:
    print('\033[m{} convertido para BINÁRIO é igual a {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('\033[m{} convertido para OCTAL é igual a {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('\033[m{} convertido para HEXADECIMAL é igual a {}.'.format(numero, hex(numero)[2:]))
else:
    print('\033[mDigite uma opção válida!!')
