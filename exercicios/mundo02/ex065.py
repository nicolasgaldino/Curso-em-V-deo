'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual
foi o maior e menor valores digitados. O programa deve perguntar 
ao usuário se ele quer ou não continuar digitando valores.'''
resposta = 'S'
soma = quant = media = maior = menor = 0
while resposta == 'S':
  num = int(input('Digite um valor inteiro: '))
  soma += num
  quant += 1
  if quant == 1:
    maior = menor = num
  else:
    if num > maior:
      maior = num
    if num < menor:
      menor = num
  resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} e média entre ele é {media:.1f}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}.')