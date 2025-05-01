peso = float(input('Informe o peso (Kg): '))
altura = float(input('Informe a altura (m): '))
imc = peso / altura**2
print('O IMC da pessoa é: {:.1f}.'.format(imc))
if imc < 18.5:
    print('A pessoa está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('Que bom! A pessoa está com o peso NORMAL.') 
elif 25 <= imc < 30:
    print('ATENÇÃO! A pessoa está com SOBREPESO (Obesidade grau I)')
elif 30 <= imc < 40:
    print('CUIDADO! A pessoa está com Obesidade grau II.')
elif imc > 40:
    print('ALERTA! A pessoa está com OBESIDADE GRAVE (grau III)')