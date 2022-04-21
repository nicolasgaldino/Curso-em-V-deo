'''Faça um programa que jogue par ou ímpar com o computador.
O programa será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.'''
cont = 0
from random import choice
escolha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
  computador = choice(escolha)
  user = int(input('Digite um valor: '))
  tot = computador + user
  tipo = ' '
  while tipo not in 'PI':
    tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
  if tipo == 'P':
    if tot % 2 == 0:
      print('Você ganhou!')
      cont += 1
    else:
      print('Você perdeu.')
      break
  elif tipo == 'I':
    if tot % 2 == 1:
      print('Você ganhou!')
      cont += 1
    else:
      print('Você perdeu.')
      break
print(f'Fim de jogo! Você venceu {cont} vezes.')