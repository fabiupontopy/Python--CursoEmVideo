sexo=str(input('Informe seu sexo [M/F]: ')).upper()[0]
while sexo not in 'MF':
    sexo=str(input('Resposta inválida. Informe seu sexo [M/F]: ')).upper()[0]
print('Resposta registrada com sucesso!')