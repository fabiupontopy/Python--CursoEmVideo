from datetime import date
atual = date.today().year
nas=int(input('Digite o ano em que você nasceu: '))
idade = atual - nas
print('O atleta tem {} anos de idade.'.format(idade))
if id > 0 and id <=9 :
    print('Classificação: MIRIM!')
elif id > 9 and id <= 14 :
    print('Classificação: INFANTIL!')
elif id > 14 and id <=19 :
    print('Classificação: JUNIOR!')
elif id > 19 and id <= 25 :
    print('Classificação: SENIOR!')
else :
    print('Classificação: MASTER! Que que há, velinho?')
print('Tenha um ótimo day! ;)')