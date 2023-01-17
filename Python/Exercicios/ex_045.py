#Faça um jogo jakenpo
from random import randint
opComputador = randint(1,3)
opcao = int(input('Escolha uma opção:\n1- Pedra\n2- Papel\n3- Tesoura\n'))
if opComputador == 1 and opcao == 1:
    print('Empate!')
elif opComputador == 1 and opcao == 2:
    print('Voce venceu!')
elif opComputador == 1 and opcao ==3:
    print('Voce perdeu!')
elif opComputador == 2 and opcao == 1:
    print('Voce perdeu!')
elif opComputador == 2 and opcao == 2:
    print('Empate!')
elif opComputador == 2 and opcao == 3:
    print('Voce ganhou!')
elif opComputador == 3 and opcao == 1:
    print('Voce ganhou!')
elif opComputador == 3 and opcao == 2:
    print('Voce perdeu!')
elif opComputador == 3 and opcao == 3:
    print('Empate!')