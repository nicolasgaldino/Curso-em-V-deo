'''
Crie um programa que converta uma temperatura
digitada em Clesius para Fahrenheit e Kelvin
'''

temp = float(input('Informe a temperatura em graus Celsius: '))
print('''{:.1f} graus Celsius em:
Kelvin é {:.1f}K;
Fahrenheit é {:.1f}F.
'''.format(temp, temp + 273, temp * 1.8 + 32))