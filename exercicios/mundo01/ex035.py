'''Desenvolva um programa que leia o
comprimento de três retas e diga ao
usuário se elas podem ou não formar um trinângulo.'''
r0 = float(input('Digite um número: '))
r1 = float(input('Digite mais um número: '))
r2 = float(input('Digite outro um número: '))
if (r0 + r1 < r2) or (r0 + r2 < r1) or (r1 + r2 < r0):
    print('Não é um triângulo.')
elif (r0 == r1) and (r0 == r2):
    print('É um triângulo equilátero.')
elif (r0 == r1) or (r0 == r2) or (r1 == r2):
    print('É um triângulo isósceles.')
else:
    print('É um triângulo escaleno.')