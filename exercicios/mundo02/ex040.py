'''Crie um programa que leia duas notas de um
aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÂO
- Média 7.0 ou superior: APROVADO'''
nota0 = float(input('Digite sua primeira nota: '))
nota1 = float(input('Digite sua segunda nota: '))
tot = (nota0 + nota1) /2
if tot < 5.0:
    print('Sua média atual é {}, infelizmente você está reprovado.'.format(tot))
elif tot == 5.0 or tot <= 6.9:
    print('Sua média atual é {}, infelizmente você está de recuperação.'.format(tot))
elif tot >= 7.0:
    print('Sua média atual é {}, parabéns! Você passou.'.format(tot))