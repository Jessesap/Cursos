#Escreva um programa que faça o computador escolher um numero de 0 a 5 e peça para o usuario adivinhar o numero
import random
lista = [0,1,2,3,4,5]
nSorteado = random.choice(lista)
a = int(input('Digite um numero entre 0 e 5: '))
if a == nSorteado:
    print('Parabens! Voce acertou.')
print('O numero sorteado foi: {}'.format(nSorteado))