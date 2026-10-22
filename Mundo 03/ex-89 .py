lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        print('Valor adicionado com sucesso.')
        lista.append(num)
    else:
        print('Valor duplicado, portanto não será adicionado...')

    sn = str(input('Quer continuar? ').upper())
    if sn not in 'SN':
        print('Essa opção não está disponível, portanto o programa será encerrado.')
        break
    if sn == 'N':
        break
lista.sort()
print('=-'*30)
print(lista)