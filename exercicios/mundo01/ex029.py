'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7 por cada KM acima do limite.'''
velox =float(input('Digite a velocidade do veículo em Km/h. '))
if velox > 80:
    tot = (velox - 80) * 7
    print('''
    Você está acima do limite de velocidade.
    Correrá em multa de R$7 a cada Km acima de 80Km/h.
    Valor da multa R${:.2f}.
    '''.format(tot))
else:
    print('Dentro do limite de velocidade, siga em frente.')