cont = 0
num=int(input('Digite um número: '))
for c in range (1,num+1) :
    if num % c == 0 :
        print('\033[0;32m{}\033[0m'.format(c), end = ' ')
        cont += 1
    else :
        print('\033[0;31m{}\033[0m'.format(c), end = ' ')
print('\nPara ser PRIMO seu número deve ser divisível somente 2 vezes. '
      'Seu número foi divisível {} vezes.'.format(cont))
if cont == 2 :
    print('Portanto, seu número é PRIMO!')
else :
    print('Portanto, seu número NÃO É PRIMO!')
