'''
Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tentagente desse ângulo.#
'''
from math import sqrt
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))
a1 = a * a
b1 = b * b
c = a1 + b1
tot = sqrt(c)
sen = a / (sqrt(c))
cos = b / (sqrt(c))
tag = a / b
print('''
Com os valores digitados temos:
Cateto oposto sendo: {};
Cateto adjacente sendo: {};
Temos a hipotenusa: {:.3f};
Com esse valores chegamos aos seguintes resultados:
Seno: {:.3f};
Cosseno: {:.3f};
Tangente: {:.3f}
'''.format(a, b, tot, sen, cos, tag))
'''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import math 
ang = float(input('Digite o ângulo desejado: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tng = math.tan(math.radians(ang))
print('O ângulo {} tem SENO de {:.2f}. \nO ângulo {} tem COSSENO de {:.2f}. \nO ângulo {} tem TANGENTE de {:.2f}.'.format(ang, sen, ang, cos, ang, tng))
--------------------------------------------------------------------------------------------------------------------------------------------------------
Esse forma de resolução é bem mais simples que a minha, mas vou manter a 
minha rodando porque foi a que eu fiz sozinho e na base de tentativa e erro.
'''