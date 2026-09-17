sn = ''
cont = 0
soma = 0
maior = 0
menor = 0
while sn != 'N':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    media = soma / cont
    #
    if num > maior :
     maior = num
    else :
        menor = num
    sn = str(input('Quer continuar? [S/N] ').upper())
print('Você digitou {} números e a média foi {:.2f}'.format(cont,media))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))
