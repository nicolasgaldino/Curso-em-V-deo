'''Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.'''
num0 = int(input('Digite um valor: '))
contador = 0
for c in range(1, num0 + 1):
    if num0 % c == 0:
        contador = contador + 1
        print(c)
print('O número {}, foi divisível {} vezes.'.format(num0, contador))
if contador == 2:
    print('{} é um número primo.'.format(num0))
else:
    print('{} não é um número primo.'.format(num0))