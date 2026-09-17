from random import randint
cont = 0
while True:
    cont += 1
    print('')
    num=int(input('Digite um número de 1 á 10: '))
    pi=str(input('Digite "P" para PAR, e "I" para IMPAR: ').upper())
    print('')
    #
    maq = randint(1,10)
    total = num + maq
    print(f'Você escolheu "{num}" e a máquina escolheu "{maq}".')
    print(f'A soma deu: {total}')
    print('')
    #
    if total % 2 == 0 :
        par = total
        if pi == 'P' and par == total :
            print('Você escolheu PAR. Você GANHOU!!!')
        if pi == 'I' and par == total:
            print('Você escolheu IMPAR. Você PERDEU!!!')
        print('=-'*20)
    #
    else :
        impar = total
        if pi == 'I' and impar == total:
            print('Você escolheu IMPAR. Você GANHOU!!!')
        if pi == 'P' and impar == total:
            print('Você escolheu PAR. Você PERDEU!!!')
        print('=-'*20)
    if cont == 3:
        print('GAME OVER.')
        break
