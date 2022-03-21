'''Refaça o desafio dos triângulos (desafio 035), acrescentando
o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''
r0 = float(input('Digite um valor refente a primeira reta do triângulo: '))
r1 = float(input('Digite um valor refente a segunda reta do triângulo: '))
r2 = float(input('Digite um valor refente a terceira reta do triângulo: '))
if (r0 + r1 < r2) or (r0 + r2 < r1) or (r1 + r2 < r0):
    print('Não é um triângulo.')
elif (r0 == r1) and (r0 == r2):
    print('É um triângulo equilátero.')
elif (r0 == r1) or (r0 == r2) or (r1 == r2):
    print('É um triângulo isósceles.')
else:
    print('É um triângulo escaleno.')