val=float(input('Digite o valor da sua compra: R$ '))
print('')
#
print('[ 1 ] À vista (Dinheiro, cheque ou pix)')#10%off
print('[ 2 ] À vista (No cartão)')#5%off
print('[ 3 ] 2X no cartão sem juros')#preço normal
print('[ 4 ] 3x ou mais no cartão com juros')#20% de juros
print('')
sel=float(input('Selecione um número para simularmos: '))
#
o1 = val - (val*10/100)
o2 = val - (val*5/100)
o3 = val
o4 = val + (val*20/100)
#
if sel == 1 :
    print('Valor a ser pago com o desconto: R$ {}'.format(o1))
#
elif sel == 2 :
    print('Valor a ser pago com o desconto: R$ {}'.format(o2))
#
elif sel == 3 :
    p = int(input('Em 1 ou 2x ? '))
    if p == 1 or p == 2 :
        print('Será {}x de R$ {:.2f}'.format(p, val / p))
    else :
        print('Não existe essa opção. Tente novamente!')
#
elif sel == 4 :
    v = int(input('Será em quantas vezes? '))
    if v < 3 :
        print('Não existe essa opção. Tente novamente!')
    else :
        print('Ficará {}X de R$ {:.2f}'.format(v, o4 / v))
else :
    print('Não existe essa opção. Tente novamente!')
