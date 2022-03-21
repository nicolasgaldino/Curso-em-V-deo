'''Faça um programa que leia o ano de nascimento
de um jovem e informe de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo de se alistar;
Seu programa também deverá mostrar o tempo
que falta ou passou do prazo.'''
from datetime import datetime
sysdata = datetime.now()
anoAtual = sysdata.year
nascimento = int(input('Informe o ano que você nasceu: '))
idade = anoAtual - nascimento
if idade < 18:
    tot = 18 - idade
    print('Dentro de {} ano(s), você deverá se alistar no serviço militar.'.format(tot))
elif idade == 18:
    print('Vá à junta militar mais próxima e se aliste.')
elif idade > 18:
    tot = idade - 18
    print('Você está fora do prazo, deveria ter se alistado há {} ano(s).'.format(tot))