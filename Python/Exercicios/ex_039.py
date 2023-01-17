from datetime import date
anoNascimento = int(input('Informe o ano de nascimento: '))
anoAtual = date.today().year
if anoAtual - anoNascimento < 18:
    print('Ainda falta {} ano(s) para voce se alistar.'.format(18-(anoAtual-anoNascimento)))
elif anoAtual - anoNascimento == 18:
    print('Dirija-se a junta de sua cidade, ja chegou o momento de se alistar.')
elif anoAtual - anoNascimento > 18:
    print('Ja passou o momento de se alistar.')