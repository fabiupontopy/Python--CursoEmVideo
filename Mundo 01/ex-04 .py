print('Levando em consideração que a cada Litro de tinta pinta 2M²:')
alt=float(input('Qual a altura dessa parede?'))
larg=float(input('Qual a largura dessa parede?'))
s=alt*larg
print('Sua parede tem a dimensão de {} x {}. E sua dimensão é de {}M².'.format(alt,larg,alt*larg))
print('Você precisará de: {:.2f}L de tinta para pinta-la.'.format(s/2))
