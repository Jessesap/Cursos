a = int(input('Informe o primeiro numero: '))
b = int(input('Informe o segundo numero: '))
if a > b:
    print('O numero {} é maior que {}.'.format(a, b))
elif b > a:
    print('O numero {} é maior que {}.'.format(b, a))
elif a == b:
    print('Os dois numeros informados são iguais.')