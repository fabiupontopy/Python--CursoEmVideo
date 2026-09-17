velocidade=float(input('Qual a velocidade atual do veículo?'))
multa = (velocidade-80)*7
if velocidade>=81:
    print('Você excedeu o limite de velocidade! Você será multado em R${:.2f}.'.format(multa))
else:
    print('Tenha um bom dia, dirija com segurança.')