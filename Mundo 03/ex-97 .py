lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota um: '))
    nota2 = float(input('Nota dois: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1,nota2],media])

    sn = str(input('Quer continuar? [S/N] '))
    if sn in 'Nn':
        break
print('-='*25)
print(f'{'No.':<4}{'Nome':<10}{'Média':>8}')
for pos, alista in enumerate(lista):
    print(f'{pos:<4}{alista[0]:<10}{alista[2]:>8}')
while True:
    print('')
    opc = int(input('Mostrar nota de qual aluno? [999 para interromper]: '))
    if opc <= len(lista)-1:
        print(f'Notas do aluno: {lista[opc][0]} = {lista[opc][1]}')
        print('-=' * 25)
    if opc == 999:
        break
print('Programa finalizado...')