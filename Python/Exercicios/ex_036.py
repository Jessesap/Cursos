#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário
#e em quantos meses ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode passar de 30% do salário ou entao o emprestimo sera negado.

vlCasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o valor do salário: '))
qtMeses = int(input('Informe a quantidade de meses que voce ira pagar o empréstimo: '))

prestação = vlCasa/qtMeses
if prestação>(salario/100)*30:
    print('Empréstimo negado, valor da prestação superior a 30%')
else: 
    print('Empréstimo aprovado, o valor das parcelas será de R${:.2f}'.format(prestação))