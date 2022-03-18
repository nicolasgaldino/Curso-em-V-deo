'''Crie um programa que leia o nome de uma
pessoa e diga se tem ela tem "SILVA", no nome.'''
nome = input('Digite seu nome: ').strip().lower()
loc = nome.find('silva')
if loc == -1:
    print('Seu nome não tem "Silva".')
else:
    print('Seu nome tem "Silva".')