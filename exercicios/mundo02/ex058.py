'''Melhore o desafio 028, onde o computador
vai 'pensar' em um número entre 1 e 10.
Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites
foram necessários para vencer.'''
from random import choice
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cont = 0
res = 'S'
while res != 'N':
    num = int(input('Digite um número inteiro entre 0 e 10. '))
    random = choice(lista)
    cont = cont + 1
    if num == random:
       print('Você precisou de {} para acertar.'.format(cont))
       res = str(input('Quer continuar? [S/N]')).upper()