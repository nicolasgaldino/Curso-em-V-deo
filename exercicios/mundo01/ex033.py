'''Faça um programa que leia três números
e diga qual é o maior e qual é o menor.'''
val0 = int(input('Digite um valor: '))
val1 = int(input('Digite mais um valor: '))
val2 = int(input('Digite outro um valor: '))
maior = val0
if val1 > maior:
        maior = val1
if val2 > maior:
        maior  = val2
print('{} maior número.'.format(maior))
menor = val0
if val1 < menor:
        menor = val1
if val2 < menor:
        menor = val2
print('{} menor número.'.format(menor))
'''Esse demorei um bocado para entender a lógica.
APós pesquisar no Google, consegui entnder.
Minha variável "maior", está sendo testada dentro
de cada condicional, enquanto o valor der "True",
as condicionais vão torcando o valor dela.'''