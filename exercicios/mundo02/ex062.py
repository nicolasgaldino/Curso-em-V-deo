'''Melhore o desafio 061, perguntando para o usuário se ele
quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos.'''
priTerm = int(input('Informe o primeiro termo: '))
raZa = int(input('Informe a razão: '))
term = priTerm
cont = 1
total = 0
mais = 10
while mais != 0:
  total = total + mais
  while cont <= total:
    print('{} '.format(term), end='')
    term += raZa
    cont += 1
  print('Pausa')
  mais = int(input('Quantos termos você quer a mais?'))
print('Fim!')