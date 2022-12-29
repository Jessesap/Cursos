#Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o ultimo nome da pessoa.
nome = str(input('Digite o nome completo de uma pessoa: ')).strip()
frnome = nome.split()
p = frnome[0]
u = frnome[len(frnome)-1]
print('O primeiro nome da pessoa é {} e o ultimo é {}'.format(p,u))