total = 0
cont = 0
cont2 = 0
menor = 0
barato = ''
while True:
    prod = str(input('Digite o nome do produto: '))
    pre = float(input('Digite o preço: R$'))
    cont2 += 1
    sn = str(input('Quer continuar?').upper())
    if pre > 1000 :
        cont += 1
    #
    if cont2 == 1:
        menor = pre
        barato = prod
    else:
        if pre < menor:
            menor = pre
            barato = prod
    #
    if sn != 'S' and sn != 'N':
        print('DIGITE SOMENTE "S" OU "N"!!!')
        break
        #
    total += pre
    if sn == 'N':
        print('FIM DO PROGRAMA')
        print(f'O total da compra foi de R$ {total}')
        print(f'Temos {cont} produto(s) custando mais de R$ 1000,00')
        print(f'O produto mais barato foi {barato} que custa R$ {menor}')
        break
