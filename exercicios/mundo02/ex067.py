'''Faça um prorgrama que mostre  tabuada de vários números, um de cada vez
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.'''
while True:
  tab = int(input('Digite um valor para ver sua tabuada: '))
  if tab < 0:
    break
  for num in range(1, 11):
    tot = num * tab
    print(f'{tab} x {num:2} = {tot}.')