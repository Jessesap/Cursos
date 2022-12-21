#Crie um algoritmo que mostre seu dobro, triplo e raiz quadrada
n = int(input('Digite um numero inteiro: '))
print('Numero escolhido: {}\nSeu dobro é: {}\nSeu triplo é: {}\nSua raiz quadrada é: {:.2f}'.format(n, n*2, n*3, pow(n,(1/2))))