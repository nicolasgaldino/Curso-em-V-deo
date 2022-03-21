'''A confederação nacional de natação precisa
de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 ano: INFANTIL
- Até 19 anos: JÚNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER'''
from datetime import datetime
sysdata = datetime.now()
anoAtual = sysdata.year
anoNascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = anoAtual - anoNascimento
if idade <= 9:
    print('Com {} anos, esse atleta pertence a categoria: MIRIM'.format(idade))
elif idade <= 14:
    print('Com {} anos, esse atleta pertence a categoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('Com {} anos, esse atleta pertence a categoria: JÚNIOR'.format(idade))
elif idade == 20:
    print('Com {} anos, esse atleta pertence a categoria: SÊNIOR'.format(idade))
elif idade > 20:
    print('Com {} anos, esse atleta pertence a categoria: MASTER'.format(idade))