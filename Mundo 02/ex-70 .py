pri=int(input('Digite o primeiro termo: ')) # de tal numero
ra=int(input('Razão da PA: ')) # pulando de tanto em tanto
termo = pri
cont = 1
while cont <= 10 : #aqui foi limitado até 10 numeros contados pelo contador.
    print('{} → '.format(termo), end='')
    termo = termo + ra
    cont = cont + 1
print('FIM')
#enquanto contador for menor ou igual a 10, digite:
#(seu termo + sua razão, limitado a um contador de 10)