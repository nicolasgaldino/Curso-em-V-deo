'''Crei um programa que leia o nome de uma
cidade e diga se começa cpm "Santos", ou não.'''
cidade = input('Diga o nome de uma cidade: ').strip().lower()
pri = cidade.split()
cid = pri[0]
loc = 'santo' in cid
if loc == False:
    print('Essa cidade não começa com "Santo" no nome.')
else:
    print('Essa cidade começa com "Santo" no nome.')