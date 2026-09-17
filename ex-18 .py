from math import sqrt
co=float(input('Comprimento do cateto oposto:'))
ca=float(input('comprimento do cateto adjacente:'))
h=(co**2+ca**2)**(1/2)
print('A Hipotenusa irá medir: {:.2f}'.format(h))

print('_____________________________________________________________')

from math import hypot
co=float(input('Comprimento do cateto oposto:'))
ca=float(input('Comprimento do cateto adjacente:'))
h=hypot(co,ca)
print('A Hipotenusa irá medir: {:.2f}'.format(h))