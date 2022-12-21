#Faça um programa que converta uma temperatura de ºC para ºf:
temp = float(input('Digite os graus em ºC para conversão: '))
conv = (temp*1.8)+32
print('{}ºC equivale a {:.1f}ºf'.format(temp, conv))