'''Crie um programa que simule o funcionamento de uma
caixa eletrônico. No início, pergunte ao usuário qual
será o valor a ser sacado (númro inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$1, R$10, R$20 e R$50'''
val = int(input('Quanto você quer sacar? R$'))
tot = val 
cedAtual = 50
totCed = 0
while True:
  if tot >= cedAtual:
    tot -= cedAtual
    totCed += 1
  else:
    if totCed > 0:
      print(f'Total de {totCed} cédulas de R${cedAtual}')
    if cedAtual == 50:
      cedAtual = 20
    elif cedAtual == 20:
      cedAtual = 10
    elif cedAtual == 10:
      cedAtual = 1
    totCed = 0
    if tot == 0:
      break