'''Escreva um programa que leia dois números inteiros
e compare-os, mostrandp na tela um mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
num0 = int(input('Digite um número inteiro: '))
num1 = int(input('Digite outro número inteiro: '))
if num0 > num1:
    print('O primeiro valor é maior.')
elif num1 > num0:
    print('O segundo valor é maior.')
elif num0 == num1:
    print('Não existe valor maior, ambos são iguais.')