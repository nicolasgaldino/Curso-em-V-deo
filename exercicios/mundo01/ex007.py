b1 = float(input('Primeiro Bimestre: '))
b2 = float(input('Segundo Bimestre: '))
tot = (b1 + b2) / 2

if tot < 6:
    print('''
    Sua nota do primeiro bimestre é {:.1f} e no segundo é {:.1f}, sua média final é de {:.1f}.
    Infelizmente você foi reprovado.
    '''.format(b1, b2, tot))
else:
    print('''
    Sua nota no primeiro bimestre é {:.1f} e no segundo é {:.1f}, sua média final é de {:.1f}.
    Parabéns, você foi aprovado.
    '''. format(b1, b2, tot))