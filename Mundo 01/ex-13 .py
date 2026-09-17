print('O carro custa R$60 por dia e R$0,15 por km.')

n1=float(input('Quantos km rodados?'))
n2=float(input('Quantos dias utilizou o carro?'))
km=n1*0.15
dia=n2*60
print('Você andou {}KM, e utilizou o carro por {} dias.'.format(n1,n2))
print('R${} pelo KM rodados e R${} pelo carro.'.format(km,dia))
print('Você deve pagar o total de R${}'.format(km+dia))
