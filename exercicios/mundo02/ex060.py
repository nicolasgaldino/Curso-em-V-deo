'''Faça um programa que leia
um número qualquer e mostre
o seu fatorial.
Ex.: 5! = 5x4x3x2x1 = 120'''
num = int(input('Digite um valor: '))
factor = num
mult = 1
while factor > 0:
  print('{}'.format(factor), end='')
  print(' x ' if factor > 1 else ' = ', end='')
  mult *= factor
  factor -= 1
print('O fatorial de {} é {}.'.format(num, mult))