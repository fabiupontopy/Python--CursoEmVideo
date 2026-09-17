cont = 0
total = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    cont += 1
    total += num
print(f'A soma dos {cont} números é {total}.')