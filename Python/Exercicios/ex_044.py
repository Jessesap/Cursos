vlProduto = float(input('Informe o valor do produto: '))
opPagamento = int(input('Escolha a opção de pagamento:\n1- À vista (Dinheiro).\n2- À vista (Cartão).\n3- No crédito 2x.\n4- No credito 3x. \n'))
if opPagamento == 1:
    print('Valor total da compra R${:.2f} com 10% desconto passa a R${:.2f}'.format(vlProduto, vlProduto-(vlProduto/100)*10))
elif opPagamento == 2:
    print('Valor total da compra R${:.2f} com 5% de desconto passa a R${:.2f}'.format(vlProduto,vlProduto-(vlProduto/100)*5))
elif opPagamento == 3:
    print('O valor total da compra R${:.2f} divididos 2 vezes sendo que cada parcela sera de R${:.2f}'.format(vlProduto,vlProduto/2))
elif opPagamento ==4:
    print('O valor total da compra R${:.2f} divididos em 3 vezes com 20% de juros cada parcela será de R${:.2f}'.format(vlProduto, (vlProduto+(vlProduto/100)*20)/3))