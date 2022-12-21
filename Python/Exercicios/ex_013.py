#Faça um algoritmo que mostre o salario de um funcionario e depois acrescente 15% de aumento.
s = float(input('Digite o valor do salario: '))
print('O valor do salario do funcionario é de R${:.2f} e após o aumento ele receberá R${:.2f}'.format(s, s+(s/100)*15))