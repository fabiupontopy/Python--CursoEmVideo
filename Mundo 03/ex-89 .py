lista = []
while True:
    val = int(input('Digite um valor: '))
    lista.append(val)
    print('Valor guardado...')
    sn = str(input('Quer continuar? [S/N] ').upper())
    if sn == 'N':
        break
    if sn not in 'SN':
        print('Opção não encontrada... Portanto, programa encerrado.')
        break

print('=-'*30)
print(f'Você digitou {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor "5" não faz parte da lista...')