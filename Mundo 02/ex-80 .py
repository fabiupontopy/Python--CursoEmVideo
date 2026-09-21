valor = int(input('Que valor você quer sacar? '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd: #o valor q quero sacar tem q ser igual ou maior a 50 (céd).
        total = total - céd #valor que quero sacar - 50 (céd)
        totcéd += 1 #aqui vai contar quantas vezes consigo tirar 50.
                    # ex: se o valor q eu queira sacar seja 101, dará p tirar 50 duas vezes, duas nota de 50.,
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} células de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0 #aqui tem que zerar, pois se não vai acumular com o "totcéd" do lá de cima
        if total == 0:
            break