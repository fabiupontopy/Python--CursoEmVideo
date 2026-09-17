print('=-'*20)
print('       Detector de Palíndromo')
print('=-'*20)
print('')
frase = str(input('Digite uma frase: ')).upper().strip()
lista = frase.split()
juntar = ''.join(lista)
cont = ''
for c in range (len(juntar)-1,-1,-1) :
    cont = cont + juntar[c]
if cont == juntar :
        print('Sua frase: "{}"'.format(juntar))
        print('Ao inverso: "{}"'.format(cont))
        print('É Palíndromo!')
else :
        print('Sua frase: "{}"'.format(juntar))
        print('Ao inverso: "{}"'.format(cont))
        print('Sua frase NÃO É PALÍNDROMO!')
