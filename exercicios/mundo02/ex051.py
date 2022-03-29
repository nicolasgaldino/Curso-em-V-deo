'''Desenvolva um programa que leia o primeiro
termo e a razão de uma P.A. No final, mostre os
10 primeiros termos dessa progressão.'''
priTerm = int(input('Informe o primeiro termo: '))
raZa = int(input('Informe a razão: '))
decTerm = priTerm + ( 10 - 1) * raZa
for c in range(priTerm, decTerm + raZa, raZa):
    print(c, end=' ')