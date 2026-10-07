maior = 0
menor = 0
lista = []
for c in range (0,5):
    lista.append(int(input(f'Digite o valor do {c}°: ')))
    if c == 0:
        maior = menor = lista[c]
    if lista[c] > maior:
        maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
for i, v in enumerate(lista):
    if v == maior:
        print(f'A posição do maior número é: {i}°')