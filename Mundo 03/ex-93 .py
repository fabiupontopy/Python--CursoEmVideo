par = impar = 0
lista = [[], []]
for c in range(1,8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
        lista[0].sort()
    else:
        lista[1].append(num)
        lista[1].sort()

print('=-'*25)
print(f'Os números Pares foram: {lista[0]}')
print(f'Os números Ímpares foram: {lista[1]}')