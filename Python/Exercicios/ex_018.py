#Faça um programa que pegue um angulo e mostre o seno o cosseno e a tangente desse angulo
import math

ang = float(input('Digite o valor do angulo: '))
print('O valor do seno, cosseno e tangente do angulo de {} são respectivamente {:.2f} {:.2f} {:.2f}'.format(ang, math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))