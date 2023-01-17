a = float(input('Informe o valor da primeira reta: '))
b = float(input('Informe o valor da segunda reta: '))
c = float(input('Informe o valor da terceira reta: '))

if a + b > c and b + c > a and a + c > b:
    if a == b and a == c:
        print('Com essas retas forma-se um triângulo equilátero.')
    elif a == b or a == c or b == c:
        print('Com essas retas forma-se um triângulo isósceles.')
    elif a != b and a != c and b != c:
        print('Com essas retas forma-se um triângulo escaleno.')
else:
    print('Impossivel formar um triangulo com essas retas')