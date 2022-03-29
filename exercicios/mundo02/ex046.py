'''Faça um programa que mostre na tela uma
contagem regressiva para estouro de fogos
de artifício, inde de 10 até 0.'''
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Feliz Ano Novo!!!')