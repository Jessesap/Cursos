#Escreva um programa que pergunte a quantidade de quilometros percorridos por um carro alugado e a quantidade de dias. 
#R$60.00 a diaria 
#R$0.15 por km

km = float(input('Digite a quilometragem percorrida: '))
qtd = int(input('Digite a quantidade de dias que o carro foi alugado: '))

tt = (km*0.15)+(60*qtd)
print('Total do valor a ser pago pelo aluguel: R${:.2f}'.format(tt))