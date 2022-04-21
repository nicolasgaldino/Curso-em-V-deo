'''Refaça o desafio 051, lendo o primeiro
termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a 
estrutura while.'''
priTerm = int(input('Informe o primeiro termo: '))
raZa = int(input('Informe a razão: '))
term = priTerm
cont = 1
while cont <= 10:
  print('{} '.format(term), end='')
  term += raZa
  cont += 1