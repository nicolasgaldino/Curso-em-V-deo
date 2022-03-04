'''Faça um programa que leia um número de
0 a 9999 e mostre na tela cada um dos dígitos
separados.'''
num = (input('Digite um valor entre 0 e 9999: '))
uni = len(num)
dez = num[2]
cen = num[1]
milh = num[0]
print('''
Você digitou {}, certo? Este número tem:
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
'''.format(num, uni, dez, cen, milh))