frase=str(input('Digite uma frase:').strip().upper())
print('A letra "C" aparece {} vezes na sua frase.'.format(frase.upper().count('C')))
print('A primeira letra "C" apareceu na {}° posição'.format(frase.find('C')+1))
print('A última letra "C" apareceu na {}°posição'.format(frase.rfind('C')+1))