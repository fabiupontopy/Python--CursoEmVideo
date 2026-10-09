lista = []
while True:
    valor=int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!')
    sn = str(input('Quer continuar? [S/N]').upper())
    if sn not in 'SN':
        print('Não existe essa opção, portanto, programa encerrado!')
        break
    if sn == 'N':
        break

print('=-'*30)
lista.sort()
print(f'Você digitou os valores: {lista}')