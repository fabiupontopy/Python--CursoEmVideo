lista = []
for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #se for o "Primeiro número" ou "Colocar diretamente no final os números que já são maiores que todos os outros"
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:      #lista[posição 0] (no caso, o primeiro número digitado em "n".
                                     #se o valor de n for menor ou igual ao numero da posição "0", verifique o próximo.
                                     # se o valor de n for menor ou igual ao numero da posição "1", verifique o próximo. E assim por diante.
                lista.insert(pos,n)  #pos = posição que quero inserir / n = valor a ser inserido
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')

#"if c == 0 or n > lista[-1]:" é responsável por identificar o primeiro número
# e os últimos, caso os números digitados pelo usuário não sejam "crescentes
# (10, 12, 20, 24...), ele cai no "else", que obrigatóriamente "pos"(posição)
# vai ser menor que "len(lista)"(posição do número do usuário), já que os primeiros
# e os últimos números já foram adicionados na lista nas primeiras linhas.