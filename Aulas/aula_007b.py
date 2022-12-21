n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
di = n1 // 2
rest = n1 % n2
print('A soma é: {}, a subtração é: {}, a divisão é: {:.3f}, a multiplicação é: {}\nA potencia é: {}'.format(s,sub,div,mult,pot))
print('A divisão inteira é: {}'.format(di), end=' ')
print('O resto da divisão ou tambem chamado módulo é: {}'.format(rest))