num=int(input('Digite um número inteiro:'))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
esc=int(input('Sua opção:'))
if esc == 1 :
    print('O número que você digitou ({}), convertido em Binário é: {}'.format(num, bin(num)[2:]))
elif esc == 2 :
    print('O número que você digitou ({}), convertido em Octal é: {}'.format(num, oct(num)[2:]))
elif esc == 3 :
    print('O número que você digitou ({}), convertido em Hexadecimal é: {}'.format(num, hex(num)[2:]))
else :
    print('Opção INVÁLIDA. Digite novamente.')
print('Tenha um bom dia! ;)')
