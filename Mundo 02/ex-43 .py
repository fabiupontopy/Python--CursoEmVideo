valor=float(input('Valor da casa: R$'))
salario=float(input('Seu salário: R$'))
ano=int(input('Em quantos anos pretende pagar?'))
#valor da parcela
meses = ano * 12
#valor a ser pago
vp = valor / meses
#30%
limite = salario * 30 / 100
#
if meses <= limite :
    print('O Valor da parcela é de {:.2f}. Isso excede o valor de '.format(vp), end='')
    print('30%, portanto, Empréstimo NEGADO!')
else :
    print('O valor da parcela é de {:.f} .O valor da parcela é '.format(vp), end='')
    print('menor que 30%, portanto, Empréstimo ACEITO!')