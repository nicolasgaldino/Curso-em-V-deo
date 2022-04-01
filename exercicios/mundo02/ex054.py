'''Crie um programa que leia o ano de nascimento de
sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores.'''
from datetime import datetime
sysdata = datetime.now()
anoAtual = sysdata.year
maiorIdade = 0
menorIdade = 0
for c in range(1, 8):
    idade = int(input('Nascimento da pessoa {}: '.format(c)))
    tot = anoAtual - idade
    if tot >= 21:
        maiorIdade = maiorIdade + 1
    else:
        menorIdade = menorIdade + 1
print('''
Dentre as 7 pessoas:
{} são maior de idade;
{} são menor de idade;
'''.format(maiorIdade, menorIdade))