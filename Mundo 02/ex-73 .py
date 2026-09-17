cont = 1
tot = 0
num = 0
while num != 999 :
    num = int(input('Digite um número [999 para parar]: '))
    cont += 1
    tot += num
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont-1, tot-999))