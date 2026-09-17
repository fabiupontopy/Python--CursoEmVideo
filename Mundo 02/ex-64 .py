mediaidade = 0
maioridade = 0
nomi = ''
contmulher = 0
for c in range (1,5) :
    print('===== {}° PESSOA ====='.format(c))
    nome = str(input('Qual o seu nome: '))
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo [M/F]? '))
    #
    mediaidade += idade
    media = mediaidade / 4
    if c == 1 :
        maioridade = idade
        nomi = nome
    if idade > maioridade and sexo in 'Mm':
        maioridade = idade
        nomi = nome
    if sexo in 'Ff' and idade < 20 :
        contmulher += 1
    #
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridade,nomi))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(contmulher))