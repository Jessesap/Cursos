nota1 = float(input('Informe o valor da primeira nota: '))
nota2 = float(input('Informe o valor da segunda nota: '))

media = (nota1+nota2)/2

if media < 5:
    print('Reprovado!')
elif 5<=media and media<6.9:
    print('Recuperação')
elif media >= 7:
    print('Aprovado!')