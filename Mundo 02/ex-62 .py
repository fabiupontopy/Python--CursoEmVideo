from datetime import date
year = date.today().year
contmaior = 0
contmenor = 0
for c in range (1,7):
    nasc=int(input('Em que ano a {}°pessoa nasceu? '.format(c).strip()))
    idade = year - nasc
    if idade >= 18 :
       contmaior += 1
    else :
        contmenor += 1
print('Ao todo tivemos {} pessoas maiorais.'.format(contmaior))
print('E, ao todo tivemos {} pessoas neném.'.format(contmenor))
