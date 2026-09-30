cont = 0
num=(int(input('Digite um número: ')),
    int(input('Digite outro: ')),
    int(input('Mais um: ')),
    int(input('Último: ')))

print(f'Você digitou os valores: {num}')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}°posição')
else:
    print('O valor "3" não foi digitado em nenhuma posição')
print('Os valores pares digitados são: ',end='')
for n in num: # o "n" simboliza cada valor. Para cada valor em "num"...
    if n % 2 == 0:
        print(n,end=', ')