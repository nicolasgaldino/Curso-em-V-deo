'''Escreva um programa que leia um número N inteiro
qualquer e mostre na tela os N primeiros elemntos
de uma sequência de Fibonacci.'''
num = int(input('Digite quantos termos você quer ver: '))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= num:
  t3 = t1 + t2
  print(' - {}'.format(t3), end='')
  t1 = t2
  t2 = t3
  cont += 1
print('Fim!')