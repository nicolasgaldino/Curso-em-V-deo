'''
Proposta do desafio:
Faça um programa que leia o salário de um dado
funcionário e mostre seu novo salário, com 15% de aumento#
'''

sal = float(input('Digite o valor do salário: '))
porc = (100 + 15) * sal
adic = porc / 100
tot = adic - sal
tud = sal + tot
print('''
Seu salário é R${:.2f} com acréscimo de 15% passará a ser {:.2f}.
'''.format(sal, tud))