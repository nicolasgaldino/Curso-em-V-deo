'''Faça um programa que leia m ano qualquer
e mostre se ele é bissexto ou não.'''

'''Resolução explicada:
from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))'''

#Minha resolução
ano = int(input('Digite um ano: '))
tot = ano % 4
if tot == 0:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))