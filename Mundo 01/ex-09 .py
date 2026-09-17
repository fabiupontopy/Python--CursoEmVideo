print('Desconto de 5%')
preço=float(input('Qual é o preço? R$'))
novo = preço - (preço*5/100)
print('Com o desconto de 5%, o que antes custava R${}, passou a custar: R${}'.format(preço,novo))