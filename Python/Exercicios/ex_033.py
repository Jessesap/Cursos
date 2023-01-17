#Crie um programa que leia 3 numeros e mostre qual é o maior e qual o menor
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))

if num1>num2 and num1>num3:
    print('O numero: {} é o maior.'.format(num1))
elif num2>num1 and num2>num3:
    print('O numero: {} é o maior'.format(num2))
elif num3>num1 and num3>num2:
    print('O numero: {} é o maior.'.format(num3))
else:
    print('um ou todos os numeros são iguais')
    
if num1<num2 and num1<num3:
    print('O numero {} é o menor.'.format(num1))
elif num2<num1 and num2<num3:
    print('O numero {} é o menor.'.format(num2))
elif num3<num1 and num3<num2:
    print('O numero {} é o menor.'.format(num3))
