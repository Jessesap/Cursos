num = int(input('Digite um numero qualquer: '))
opcao = int(input('Informe a opção de conversão desejada:\n1-Binário\n2-Octal\n3-Hexadecimal\n'))
if opcao == 1:
    print('O numero {} corresponde à {} em binário.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O numero {} corresponde à {} em octal. '.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O numero {} corresponde à {} em hexadecimal.'.format(num, hex(num)[2:]))
