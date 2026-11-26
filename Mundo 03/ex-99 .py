from random import randint
from operator import itemgetter
from time import sleep

dic = {'Jogador1':randint(1,5),
       'Jogador2':randint(1,5),
       'Jogador3':randint(1,5),
       'Jogador4':randint(1,5),}
maior = list()

for a,b in dic.items():
    sleep(0.5)
    print(f'O "{a}" tirou "{b}" no dado.')

print('=-'*20)
print('== RANKING DOS JOGADORES ==')
maior = sorted(dic.items(),key=itemgetter(1),reverse=True)
for c,d in enumerate(maior):
    print(f'{c+1}° lugar: "{d[0]}" tirou "{d[1]}"')