#Crie um programa que leia 3 retas e diga se ele pode ou nao formar um triangulo
a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
if (a+b)>c and (a+c)>b and (b+c)>a:
    print('Pode-se formar um triangulo a partir das 3 retas informadas.')
else:
    print('As 3 retas não podem formar um triangulo')