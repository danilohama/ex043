"""Desenvolva uma lógica que leia o peso e altura de pessoa, calcule o IMC e mostre seu stratus, de acordo com a tabela
abaixo:
> Abaixo de 18,5: ABAIXO DO PESO
> Entre 18,5 e 25: PESO IDEAL
> 25 até 30: SOBREPESO
> 30 até 40: OBESIDADE
>Acima de 40: OBSIDADE MÓRBIDA
"""
peso = float(input('Qual é o seu peso? (Kg): '))
altura = float(input('Qual é a sua altura (m): '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25:  # elif imc <= 18.5 and imc < 25:
    print('Parabéns você está na faixa de peso normal')
elif 25 <= imc < 30:  # elif imc >= 25 and imc >= 30:
    print('você está em SOBREPESO')
elif 30 <= imc < 40:  # elif imc >= 30 and imc >= 40:
    print('Você está em OBSIDADE!')
else:
    print('OBSIDADE MORBIDA, Procure ajuda médica!')
