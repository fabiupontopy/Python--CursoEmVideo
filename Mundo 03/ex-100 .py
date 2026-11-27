from datetime import datetime
dic = {}
dic['nome']=str(input('Nome: '))
dic['idade']=int(input('Ano em que nasceu: '))
dic['ctps']=int(input('Carteira de Trabalho (0 para "não tem"): '))
if dic['ctps'] != 0:
    dic['contratação']=int(input('Ano de Contratação: '))
    dic['salário']=int(input('Salário: R$ '))
    dic['aposentadoria'] = (dic['contratação'] + 35) - dic['idade']

print('=-'*20)
for a,b in dic.items():
    print(f'-{a} tem o valor de "{b}".')
