from random import randint
lista = list()
coplista = list()

quant = 1
jog = int(input('Quantos jogos você quer que eu sorteie? '))

while quant <= jog:
    while len(lista) < 6:
        num = randint(1,60)

        if num not in lista:
            lista.append(num)

    lista.sort()
    coplista.append(lista[:])
    lista.clear()
    quant += 1

for l in coplista:
    print(f'{l}')