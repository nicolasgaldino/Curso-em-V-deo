'''Faça um programa que leia o pesoa de
5 pessoas e no final mostre qual foi o
maior e o menor peso lidos.'''
maior = 0
menor = 0
for c in range(1, 6):
    pess = float(input('Peso da pessoa {}: '.format(c)))
    if c == 1:
        maior = pess
        menor = pess
    else:
        if pess > maior:
            maior = pess
        if pess < menor:
            menor = pess
print('''
O maior peso lido foi: {}Kg
O menor peso lido foi: {}Kg
'''.format(maior, menor))