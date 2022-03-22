'''Escreva um programa para aprovar um empréstimo
bancário para a compra de uma casa. O programa vai
perguntar o valor da casa, o salário do comprador,
e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que
ele não pode exceder 30% do salário ou então o
empréstimo será negado.'''
valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual sua renda mensal? R$'))
anos = int(input('Pretende pagar a casa por quantos anos? '))
meses = 12 * anos
parcelas = valor / meses
porcentSalario = salario * (30 / 100)
if parcelas >= porcentSalario:
    print('''
    Com sua renda mensal atual, o financiamento não pôde ser aprovado.
    As parcelas irão exceder 30% do seu salário.
    Você pagará R${:.2f}, em {} meses. 
    '''.format(parcelas, meses))
else:
    print('''
    Parabéns, seu empréstimo foi aprovado!
    Você pagará R${:.2f}, em {} meses.
    '''.format(parcelas, meses))