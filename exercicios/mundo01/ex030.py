'''Crie um programa que leia um númro inteiro
e mostre na tela se é PAR ou ÍMPAR.'''
parimp = int(input('Digite um número: '))
tot = parimp % 2
if tot == 0:
    print('{} é um número par.'.format(parimp))
else:
    print('{} é um número ímpar.'.format(parimp))