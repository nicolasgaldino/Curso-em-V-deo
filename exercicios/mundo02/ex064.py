'''Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No
final, mostre quantos números foram digitados e qual
foi a soma entre ele. (Desconsiderando o flag).'''
val = 0 # val = cont = som = 0
cont = 0
soma = 0
val = int(input('Digite o número [999] para interromper o programa. '))
while val != 999:
  soma += val
  cont += 1
  val = int(input('Digite o número [999] para interromper o programa. '))
print(f'Você digitou {cont} e a soma entre todos ele é {soma}.')