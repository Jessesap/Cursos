#Crie um programa que pergunta quantos reais ela tem na carteira e quantos dolares ela pode comprar 1$ == 3.27R$
vl = int(input('Digite quantos reais voce tem na carteira: '))
print('Com R${:.2f} reais voce compra ${:.2f} dolares.'.format(vl, vl/3.27))