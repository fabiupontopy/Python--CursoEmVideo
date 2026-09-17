f = 1
n=int(input('''Digite um número para
calcular seu fatorial: '''))
while n > 0 :
    f = f * n
    if n > 1:
        print('{} X'.format(n), end=' ')
    else:
        print('{} = {}'.format(n,f), end=' ')
    n = n - 1
#aqui deve ser somente no final do código (else), pois se for antes,
# o loop irá terminar porque vai de 3 → 2 → 1 → 0, e aí "p > 0" não é mais verdadeiro.
#Lá em cima é: "Enquanto "pn for maior que "0".