n1 = int(input('Digite um número: '))
print('''
O dobro de {} vale {};
O triplo de {} vale {};
A raíz quadrada de {} é {:.3f};
'''.format(n1, n1 * 2, n1, n1 * 3, n1, n1 ** (1/2)))