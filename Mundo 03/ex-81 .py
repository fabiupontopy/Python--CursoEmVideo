cont = ('zero','um','dois','três','quatro',
        'cinco','seis','sete','oito','nove',
        'dez','onze','doze','treze','catorze',
        'quinze','dezesseis','dezessete','dezoito',
        'dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Não existe essa opção, tente novamente. ',end='')
    else:
        print(f'O número que você digitou foi {cont[num]}.')
        break
