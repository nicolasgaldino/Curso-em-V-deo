'''Crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo, desconsiderando
os espaços.'''
frase = str(input('Digite uma frase: ')).strip().upper() #analiso a frase
palavras = frase.split() #separa a frase
junto = ''.join(palavras) #junta em uma única string
inverso = ''
for letra in range(len(junto) -1, -1, -1): #faz o inverso da frase digitada
    inverso = inverso + junto[letra]
if inverso == junto:
    print('''
    A frase:
    {}
    É um palíndromo.
    '''.format(frase))
else:
    print('''
    A frase:
    {}
    Não é um palíndromo.
    '''.format(frase))