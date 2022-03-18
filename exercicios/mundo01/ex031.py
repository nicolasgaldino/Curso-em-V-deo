'''Desenvolva um programa que pergunta a distância de
uma viagem em Km. Calcule o preço da passagem, cobrando
R$0.50 por Km para viagens de até 200Km e R$0.45 para
viages mais longas.'''
dist = float(input('Digite a distância da viagem em Km/h: '))
if dist <= 200:
    tot = dist * 0.50
    print('Sua viagem vai custar R${:.2f}.'.format(tot))
else:
    tot = dist * 0.45
    print('Sua viagem vai custar R${:.2f}.'.format(tot))