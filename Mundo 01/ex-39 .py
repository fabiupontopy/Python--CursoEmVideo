print('-=' * 20)
print('Analisador de Triangulos')
print('-=' * 20)
a=float(input('Primeiro segmento:'))
b=float(input('Segundo segmento:'))
c=float(input('Terceiro segmento'))
if a < b + c and b < a + c and c < a + b:
    print('Os Segmentos acima formam um triângulo!')
else:
    print('Os Segmentos acima NÃO formam um triângulo!')
