n1=float(input('Digite um número:'))
n2=float(input('Digite outro número:'))
n3=float(input('Mais um:'))
#maior
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))