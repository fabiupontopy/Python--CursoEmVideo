print('Qual o seu Sexo?')
sexo=str(input('Digite [H] para homem, ou [M] para mulher: '))
nas=int(input('Digite seu ano de nascimento:'))
idade = 2026 - nas
if sexo == 'M' :
    print('Parabéns! Você esta dispensada.')
    print('Quem nasceu em {} tem {} anos em 2026.'.format(nas, idade))
#para quem já passou do tempo (até 5 anos)
elif sexo == 'H' and idade >= 18 and idade <= 23 :
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
    print('Seu alistamento deveria ser feito em {}.'.format(nas + 18))
#para menor de 18 anos
elif sexo == 'H' and idade < 18 :
    print('Ainda faltam {} anos para seu alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(nas + 18))
#para quem passou de 5 anos (6 anos ou mais)
elif sexo == 'H' and idade >= 24 :
    print('Você tem que se alistar IMEDIATAMENTE!')
