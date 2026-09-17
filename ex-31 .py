print('Média')
n=str(input('Digite seu nome:'))
n1=float(input('Digite sua nota de Matemática:'))
n2=float(input('Digite sua nota de Português:'))
media = (n1+n2)/2
print('Sua Média é: {}'.format(media))
if media >=6 :
    print('Parabéns pela nota, {}!'.format(n))
else :
    print('Nota baixa, estude mais, {}!'.format(n))
