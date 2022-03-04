'''Faça um programa que leia uma frase pelo
teclado e mostre:
Quantas vezes aparece a letra "a"
Em que posição ela aparece primeiro
Em que posição ela aparece por último'''
frase = str(input('Digite uma frase: ')).lower()
qua = frase.count('a')
lug = frase.strip().find('a')
ult = frase.rfind('a')
print('''
Nesta frase a letra "a" aparece {} vezes;
Aparece pela primeira vez em: {};
E aparece pla última vez em: {};
'''.format(qua, lug))
