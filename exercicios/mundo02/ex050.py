'''Desenvolva um programa que leia seis
números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.'''
acumulador = 0
contador = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        contador = contador + 1 #contador += 1
        acumulador = acumulador + n #acumulador += n
print('''
Dentre os 6 valores digitados, {} são par e a soma dele respectivamente é igual a: {}
'''.format(contador, acumulador))