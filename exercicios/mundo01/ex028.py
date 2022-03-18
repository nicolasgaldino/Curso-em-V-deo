'''Escreva um programar que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário
venceu ou perdeu.'''
from random import choice
lista = [0, 1, 2, 3, 4, 5]
random = choice(lista)
num = int(input('Digite um número inteiro entre 0 e 5. '))
if num == random: 
    print('Parabéns! Você acertou o número que eu estava pensando.')
else:
    print('Você errou, eu estava pensando no {}.'.format(random))
    