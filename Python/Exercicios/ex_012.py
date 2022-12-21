#Faça um algoritmo que receba o valor de um produto e mostre o valor deste mesmo produto com 5% de desconto.
vl = float(input('Digite o valor do produto: '))
print('O valor do produto é de R${}, e com o desconto passa a ser R${}'.format(vl,vl-(vl/100)*5))