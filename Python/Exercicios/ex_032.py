#Crie um programa que leia se o ano é bissexto ou não
from calendar import isleap
ano = int(input('Digite um ano qualquer: '))
if isleap(ano):
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))