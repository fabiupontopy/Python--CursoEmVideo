maior = menor = 0
lista = list()
principal = list()
while True:
    lista.append(str(input('Digite seu nome: ')))
    lista.append(float(input('Digite seu peso: ')))

    if len(principal) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    principal.append(lista[:])
    lista.clear()

    sn = str(input('Deseja continuar? [S/N] '))
    if sn in 'Nn':
        break

print('=-'*25)
print(f'Foram cadastradas {len(principal)} pessoas.')
print(f'O mais pesado foi {maior}kg; sendo eles: ',end='')
for c in principal:
    if c[1] == maior:
        print(f'[{c[0]}]',end='')
print()
print(f'O mais leve foi {menor}kg; sendo eles: ',end='')
for c in principal:
    if c[1] == menor:
        print(f'[{c[0]}]',end='')