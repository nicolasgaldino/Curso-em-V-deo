'''Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre
o comprimento da hipotenusa.
----------------------------------------------------------------'''
from math import sqrt
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))
a1 = a * a
b1 = b * b
c = a1 + b1
tot = sqrt(c)
print('O comprimento da hipotenusa é de {:.2f}.'.format(tot))

'''
from math import hypot
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(a, b)
print('O comprimento da hipotenusa é de {:.2f}.'.format(hip))
----------------------------------------------------------------
Anotei a resolução porque ela é muito mais simples que o meu
jeito de fazer, mas de qualquer forma deixarei a minha solução
rodando.
'''