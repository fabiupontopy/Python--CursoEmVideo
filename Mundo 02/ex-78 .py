cont = 0
cont2 = 0
cont3 = 0
while True:
    homens = ''
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ').upper())
    print('=-'*20)
    sn = str(input('Quer continuar? [S/N] ').upper())
    #
    if sexo == 'M':
        cont += 1
    if idade >= 19:
        cont2 += 1
    if sexo == 'F' and idade < 20:
        cont3 += 1
    #
    if sn == 'N':
        print('=-'*20)
        print(f'Total de pessoas com mais de 18 anos: {cont2}')
        print(f'Total de homens cadastrados: {cont}')
        print(f'Total de mulheres com menos de 20 anos: {cont3}')
        break
