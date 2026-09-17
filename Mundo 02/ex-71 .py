pri = int(input('Primeiro termo: '))
ra = int(input('Razão da PA: '))
tot = pri
mais = 10
cont_total = 0
while mais != 0:
    cont = 1
    while cont <= mais:
        print('{} → '.format(tot), end='')
        tot += ra
        cont += 1
        cont_total += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('O Programa foi finalizado com {} termo mostrados.'.format(cont_total))
