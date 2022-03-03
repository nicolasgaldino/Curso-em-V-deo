import math
num = int(input('Digite um número e descubra sua raíz quadrada: '))
rnum = math.sqrt(num)
print('Você digitou {}, certo? OK! A raíz quadrada deste número é {}.'.format(num, math.ceil(rnum)))