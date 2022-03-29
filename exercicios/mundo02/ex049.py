'''Refaça o desafio 009, mostrando a tabuada de um
número que o usuário escolher, só que agora utilizando
um laço for.'''
num = int(input('Digite um valor: '))
for c in range(1, 11):
    tot = c * num
    print('{} x {:2} = {}'.format(num, c, num * c))