soma = 0
contador = 0
for c in range (1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0 :
        soma = soma + n
        contador = contador + 1
print('Tem {} números pares. A soma deles é {}.'.format(contador,soma))