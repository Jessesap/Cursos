#Crie um programa que leia uma frase e diga:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

frase = str(input('Digite a frase a ser analisada: '))

print('A letra A aparece {} vezes na frase, sendo a primeira aparição na posicão: {} e a ultima na posição  {}'.format(frase.count('A'),frase.find('A')+1, frase.rfind('A')+1))