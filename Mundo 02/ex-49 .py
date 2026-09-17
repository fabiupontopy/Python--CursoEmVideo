a=float(input('Digite o primeiro segmento: '))
b=float(input('Digite o segundo segmento: '))
c=float(input('Digite o terceiro segmento: '))
if a + b > c and a + c > b and b + c > a :
    print('É possível formar um Triângulo!')
    if a == b == c :
        print('Triângulo Equilátero')
    if a != b != c != a:
        print('Triângulo Escaleno')
    else :
        print('Triângulo Isósceles')
else :
    print('Os segmentos acima não formam um triângulo!')