#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
n = int(input('Digite um numero de 0 a 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('O numero possui: \n{} unidades\n{} dezenas\n{} centenas\n{} milhares'.format(u, d, c, m))