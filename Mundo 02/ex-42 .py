nome=str(input('Digite seu nome:').strip())
if nome == 'Fábio' :
    print('Seu nome é bonito, {}!'.format(nome))
elif nome == 'Lucas' or nome == 'Matheus' :
    print('Seu nome é bem comum, {}.'.format(nome))
elif nome == 'Jason' or nome == 'Michael' :
    print('Seu nome é bem diferenciado, {}!'.format(nome))
else :
    print('Não gostei do seu nome.')
print('Tenha um ótimo dia.')
