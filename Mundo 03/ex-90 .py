lista = []
par = []
impar = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    sn = str(input('Quer continuar? [S/N] ').upper())
    if sn not in 'SN':
        print('Opção não encontrada, portanto programa encerrado...')
        break
    if sn in 'N':
        break
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de impares é: {impar}')