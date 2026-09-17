n1=float(input('Primeira nota:'))
n2=float(input('Segunda nota:'))
media = (n1 + n2) / 2
if media > 7 :
    print('Sua média final foi {}. Você está aprovado!'.format(media))
elif media >= 5 and media <= 7 :
    print('Sua média final foi {}. Você está de recuperação!'.format(media))
elif media <= 4 :
    print('Sua média final foi {}. Você está reprovado!'.format(media))