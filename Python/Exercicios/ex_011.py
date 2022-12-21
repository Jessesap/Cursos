#Faça um programa que leia a largura e a altura de uma parede, calcule sua area e diga a
#quantidade de tinta necessaria para pinta-la. 1l == 2m².
h = float(input('Digite a altura da parede: '))
w = float(input('Digite a largura da parede: '))

print('A area da parede de {} metros de altura e {} metros de largura é de: {} e voce precisará de {:.1f} litro(s) de tinta'.format(h,w, h*w, (h*w)/2))