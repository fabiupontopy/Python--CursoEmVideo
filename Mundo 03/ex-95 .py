matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = 0
num = 0
for c in range(0,3):
    for l in range(0,3):
        matriz[c][l]=int(input(f'Digite um valor [{c}, {l}]: '))

        if matriz[c][l] % 2 == 0:
            par += matriz[c][l]

print('=-'*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('=-'*30)

print(f'A soma dos valores pares é: {par}.')

soma = (matriz[0][2])+(matriz[1][2])+(matriz[2][2])
print(f'A soma dos valores da terceira coluna é: {soma}.')

maior = max(matriz[1])
print(f'O maior valor da segunda linha é: {maior}.')