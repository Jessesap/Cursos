#Faça um programa que receba o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e 
#mostre o comprimento da hipotenusa
import math
op = float(input('Digite o comprimento do cateto oposto: '))
ad = float(input('Digite o comprimento do cateto adjacente: '))

hip = math.sqrt(pow(op, 2)+(pow(ad, 2)))
print('O valor da hipotenusa de um triangulo com comprimento do cateto oposto igual a {} e adjacente igual a {} é {:.2f}'.format(op, ad, hip))