'''Faça um programa que leia o nome de completo
de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.'''
n = str(input('Qual é o seu nome? ')).strip()
nome = n.split()
print('É um prazer te conhecer, {}!'.format(n))
print('Seu primeiro nome é: {};'.format(nome[0]))
print('Seu último nome é: {};'.format(nome[len(nome)-1]))