frase = 'Nem que eu ande pelo vale da sombra da Morte'
espFrase = "      nao temerei        "
#Para manipular o texto da frase dessa forma o padrao é: (frase[inicio:fim:passe])
print(frase[0::4])
#Para medir o comprimento da frase
print(len(frase))
#para contar quantas vezes um determinado caracter aparece na frase
print(frase.count('e'))
#Para contar quantas vezes um determinado caracter aparece num intervalo da frase
print(frase.count('a', 0, 15))
#Para encontrar onde uma determinada parte do texto esta na string
print(frase.find('ande'))
#Se voce coloca uma string que nao existe na cadeia de caracter o programa te retorna o valor -1
print(frase.find('algum'))
#Retorna um valor True ou false se a frase possui ou não uma determinada string
print('Curso' in frase)
#Com o replace voce pode substitutir uma determinada string dentro de uma string
modFrase = frase.replace('Morte', 'escuridão')
print(modFrase)
#Para deixar todos os caracteres da string aiuscula
print(frase.upper())
#Para deixar todos os caracteres da string minusculas
print(frase.lower())
#Para deixar apenas a primeira letra maiuscula
print(frase.capitalize())
#Para colocar todas as primeiras letras das palavras em Maiusculo
print(frase.title())
#Para tirar os espacos no comeco e no final da frase
print(espFrase.strip())
#Para remover os espacos do lado esquerdo(left) e direito(right) da frase
print(espFrase.lstrip())
print(espFrase.rstrip())
#Para gerar uma lista de uma frase usa o split, que divide o texto da string pelos espaços
fr = frase.split()
print(fr)
#Para juntar uma lista e transforma-la em uma unica string usa-se o join
print(' '.join(fr))
