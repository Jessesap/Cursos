#Crie um programa que leia um salario e calcule o aumento, sendo que:
#Acima de 1250 reais == 10%
#Inferiores a 1250 reais o aumento é de 15%
salario = float(input('Informe o valor do salario: '))
if salario>1250:
    print('O salario após o reajuste é de R${:.2f}'.format(salario + ((salario/100)*10)))
elif salario <1250:
    print('O salario após o reajuste é de R${:.2f}'.format(salario + ((salario/100)*15)))
else:
    print('Parabens voce foi premiado, se seu salario é de R$1250.00 voce se lascou')