'''Faça um programa que leia o nome de completo
de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.'''
n = str(input('Qual é o seu nome? ')).strip()
nome = n.split()
print('''
É um prazer conhecê-lo, {}!
Seu primeiro nome é {};
Seu segundo nome é {};
'''.format(n, (nome[0]), (nome[len(nome)-1])))