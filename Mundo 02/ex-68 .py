from time import sleep
p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
op = 0
while op != 5:
    sleep(0.5)
    print('     [ 1 ] SOMAR')
    print('     [ 2 ] MULTIPLICAR')
    print('     [ 3 ] MAIOR')
    print('     [ 4 ] NOVOS NÚMEROS')
    print('     [ 5 ] SAIR DO PROGRAMA')
    sleep(0.7)
    op = int(input('Selecione uma opção: '))
    sleep(1)
    print('=-=' * 20)
    sleep(1)
    print('Loading...')
    sleep(1)
    #
    if op == 1: #somar
        print('A soma entre os dois números é: {:.1f}'.format(p+s))
    if op == 2: #multiplicar
        print('A multiplicação entre os dois números é: {:.1f}'.format(p*s))
    if op == 3: #maior
        if p > s :
            maior = p
        if s > p :
            maior = s
        print('O maior número é: {}.'.format(maior))
    if op == 4: #novos números
        p=int(input('Primeiro valor:'))
        s=int(input('Segundo valor:'))
    if op not in range(1,6) :
        print('NÃO existe essa opção!')
    sleep(1)
    print('=-=' * 20)
sleep(2)
print('Sessão finalizada!')
