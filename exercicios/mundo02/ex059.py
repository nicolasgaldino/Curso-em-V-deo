'''Crie um programa que leia dois valores e
mostre um nedu na tela:
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Encerrar o programa
Seu programa deverá realizar a operação
solicitada em cada caso.'''
valor0 = int(input('Digite um valor: '))
valor1 = int(input('Digite mais um valor: '))
opcao = str(input('''
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Encerrar o programa
''')).strip()
while opcao != '5':
  if opcao == '1':
    tot = valor0 + valor1
    print('A soma entre {} e {} é igual a {}'.format(valor0, valor1, tot))
    opcao = str(input('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Encerrar o programa
    ''')).strip()
  elif opcao == '2':
    tot = valor0 * valor1
    print(tot)
    opcao = str(input('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Encerrar o programa
    ''')).strip()
  elif opcao == '3':
   if valor0 > valor1:
    print(valor0)
    opcao = str(input('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Encerrar o programa
    ''')).strip()
   else:
    print(valor1)
    opcao = str(input('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Encerrar o programa
    ''')).strip()
  elif opcao == '4':
    valor0 = int(input('Digite um valor: '))
    valor1 = int(input('Digite mais um valor: '))
    opcao = str(input('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Encerrar o programa
    ''')).strip()