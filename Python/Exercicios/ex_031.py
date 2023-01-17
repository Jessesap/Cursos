#Crie um programa que leia a distancia de uma viagem e calcule o preço sendo que:
#ate 200km cada km é 50 centavos, acima disso fica 45
distancia = float(input('Digite a distancia percorrida: '))
if distancia <= 200:
    print('O total da viagem é de R${:.2f}'.format(distancia*0.50))
else:
    print('O total da viagem é de R${:.2f}'.format(distancia*0.45))