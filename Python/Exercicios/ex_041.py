from datetime import date

anoAtual = date.today().year

anoNascimento = int(input('Informe o ano de nascimento: '))

if anoAtual - anoNascimento<= 9:
    print('Categoria Mirim')
elif anoAtual - anoNascimento > 9 and anoAtual - anoNascimento<=14:
    print('Categoria Infantil')
elif anoAtual - anoNascimento > 14 and anoAtual - anoNascimento <=19:
    print('Categoria Junior')
elif anoAtual - anoNascimento == 20:
    print('Categoria Senior')
elif anoAtual-anoNascimento >20:
    print('Categoria Master')