sal=float(input('Qual o salário do funcionário? R$'))
if sal > 1249 :
    novo = sal + (sal * 15 / 100)
else :
    novo = sal + (sal * 10 / 100)
print('O Salário de R$ {:.2f} passará a ser R$ {:.2f}'.format(sal, novo))