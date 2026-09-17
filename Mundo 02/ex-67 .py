from random import randint
p = randint(0,10)
cont = 0
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
print('=-'*25)
num=int(input('Qual o seu palpite? '))
while num > 10:
    num = int(input('Você deve escolher entre 0 e 10 somente. Tente novamente, qual o seu palpite? '))
while num < p:
    num=int(input('Mais... Qual o seu palpite? '))
    cont += 1
while num > p:
    num=int(input('Menos... Qual o seu palpite? '))
    cont += 1
print('Você acertou com {} tentativas. Parabéns!'.format(cont))
