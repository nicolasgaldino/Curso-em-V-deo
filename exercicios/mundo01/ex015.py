'''
Crie um programa que pergunte quantos quilômtros foram percorridos
por um carro e quantos dias ele esteve alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
'''

dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos quilômetros você percorreu com o carro? '))
aludia = dias * 60
rodkm = km * 0.15
tot = aludia + rodkm
print('''
O veículo esteve alugado por {} dias, e rodou {}Km assim o total a pagar é: R${:.2f}.
'''.format(dias, km, tot))