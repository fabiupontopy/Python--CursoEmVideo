distancia = float(input('Qual a distância percorrida? '))
npromo = distancia * 0.50
promo = distancia * 0.45
if distancia < 199:
    print('O valor da sua passagem será de R${:.2f}'.format(npromo))
else:
    print('O valor da sua passagem será de R${:.2f}'.format(promo))