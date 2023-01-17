#Escreva um programa que receba a velocidade de um carro
#Se ele estiver acima de 80km/h ele sera multado em um valor de 7 x a quantidade de quilometros a mais
velocidade = float(input('Informe a velocidade do carro: '))
if velocidade > 80:
    vlMulta = (velocidade-80)*7
    print('Voce foi multado, o valor da multa a ser pago é de: {:.2f}'.format(vlMulta))
else:
    print('Voce não recebeu nenhuma multa pois estava abaixo do limite de velocidade.')