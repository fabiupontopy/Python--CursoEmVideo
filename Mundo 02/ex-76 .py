while True:
    num = int(input('Digite um número: '))
    print('=-' * 30)
    if num < 0:
        print('Programa encerrado...')
        break
    for c in range (1,11):
        print(f'{num} X {c} = {num*c}')
    print('=-' * 30)