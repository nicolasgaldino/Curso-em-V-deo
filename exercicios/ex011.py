lar = float(input('Digite a largura: '))
alt = float(input('Digite a altra: '))
dim = lar * alt
area = dim / 2
print('''
Sua parede tem uma dimensão de {} x {} com uma área equivalente a {:.2f}m².
Para pintá-la serão necessários {:.2f} litros de tinta.
'''.format(lar, alt, dim, area))

#cálculo para descobrir a área é altura x largura, tendo
#tendo o valor da área eu divido por 2, já que quero saber
#quantos liros de tinta vou usar para pintar a área inteir
#tendo como refência 1 litro de tinta pinta 2 metros quadrados