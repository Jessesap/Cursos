#Crie um programa que leia o nome de uma pessoa e diga se ela tem ou não Silva no nome
nome = str(input('Digite o nome completo da pessoa: '))

frnome = nome.split()
print('A pessoa possui Silva no nome? {}'.format('Silva' in frnome))