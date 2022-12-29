#Crie um programa que leia o nome completo da pessoa e mostre:
#Nome com todas as letras maiusculas
#Nome com todas as letras minusculas
#Quantas letras tem ao todo menos os espaços
#Quantas letras tem o primeiro nome
nome = input('Digite seu nome completo: ')

print(nome.upper())
print(nome.lower())
tFrase = len(nome)
qtEspaco = nome.count(' ')
qtLetras = tFrase - qtEspaco
print('O total de letras sem espaços é de: {}'.format(qtLetras))
loc = nome.find(' ')
print('O primeiro nome tem {} letras'.format(loc))