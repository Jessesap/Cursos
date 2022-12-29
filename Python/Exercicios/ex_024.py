#Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome Santo
city = str(input('Digite o nome da cidade: '))

ftcity = city.split()

print('A cidade comeca com Santo? {}'.format('Santo' in ftcity[0]))