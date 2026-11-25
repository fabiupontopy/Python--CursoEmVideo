aluno = dict()
aluno['Nome']=str(input('Digite seu nome: ')) #nome: fabio
aluno['Média']=float(input(f'Digite a média de {aluno['Nome']}: ')) #media: 7.5"
print('=-'*20)
if aluno['Média'] >= 7:
    print('Situação: APROVADO')
if aluno['Média'] == 6:
    print('Situação: RECUPERAÇÃO')
if aluno['Média'] <= 5:
    print('Situação: REPROVADO')
for nom,med in aluno.items():
    print(f'{nom} é igual a {med}')
    
#acima de 7 = aprovado
#abaixo de 7 = recuperação
#abaixo de 5 = reprovado