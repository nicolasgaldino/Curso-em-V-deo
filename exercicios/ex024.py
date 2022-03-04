'''Crei um programa que leia o nome de uma
cidade e diga se começa cpm "Santos", ou não.'''
cidade = input('Diga o nome de uma cidade: ')
loc = 'Santo' in cidade
if loc == False:
    print('Essa cidade não começa com "Santo" no nome.')
else:
    print('Essa cidade começa com "Santo" no nome.')