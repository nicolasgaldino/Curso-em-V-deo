#Crie um programa que leia um número real qualquer
#pelo teclado e mostre na tela sua porção inteira.
#Ex.: Digite um número: 6.127
#O número 6.127 tem a parte inteira 6.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import math
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num, math.floor(num)))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Esse desafio tem um problema! Se o usuário digitar algum número 
#com '.6' ou '.4' o número só será arredondado para cima ou para baixo.
#Tentei implementar uma condicional que identificasse, mas não estou sabendo.#

#import math
#num = float(input('Digite um número: '))
#if num <= float(.5):
#    print('O número {} tem a parte inteira {}.'.format(num, math.ceil(num)))
#else:
#    print('O número {} tem a parte inteira {}.'.format(num, math.floor(num)))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Como dá para ver, eu pensei em algo bem elaborado, mas me estressei
#tentando descobrir o porquê dos resultados sempre terem final ".0",
#e assim fazendo a função ignorar o 'if', indo direto para o 'else'.

#import math
#num = int(input('Digite um número e veja sua raíz quadrada: '))
#rnum = math.sqrt(num)
#if num == int():
#    print('Você digitou {}, certo? A raíz quadrada deste número é {}.'.format(num, math.trunc(rnum)))
#else:
#    print('Você digitou {}, certo? A raíz quadrada deste número é {}. \nEsse número tem dízima periódica, sua porção inteira é {}'.format(num, rnum, math.ceil(rnum)))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------