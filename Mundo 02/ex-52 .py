from random import randint
from time import sleep
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador=int(input('Qual opção você escolhe? Digite um número: '))
#
p = randint(0,2)
lista = ['Pedra', 'Papel', 'Tesoura']
maquina = lista[p]
#
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(0.5)
print('TESOURA')
sleep(0.5)
print('=-' * 30)
if jogador == 1 :
    print('Jogador = Pedra')
if jogador == 2 :
    print('Jogador = Papel')
if jogador == 3 :
    print('Jogador = Tesoura')
sleep(2)
print('Computador = {}'.format(maquina))
print('=-' * 30)
sleep(1)
#
if maquina == 'Pedra' :
    if jogador == 1 :
        print('EMPATE!')
    elif jogador == 2 :
        print('Você GANHOU!!!')
    elif jogador == 3 :
        print('Você PERDEU!')
    else :
        print('Error')
#
if maquina == 'Papel' :
    if jogador == 1 :
        print('Você PERDEU!')
    elif jogador == 2 :
        print('EMPATE!')
    elif jogador == 3 :
        print('Você GANHOU!!!')
    else:
        print('Error')
#
if maquina == 'Tesoura' :
    if jogador == 1 :
        print('Você GANHOU!!!')
    elif jogador == 2 :
        print('Você PERDEU!')
    elif jogador == 3 :
        print('EMPATE!')
    else :
        print('Error')