'''Escreve um programa que pergunte o salário de
um funcionário e calcule o valor de seu aumento.
Para salários superiores a R$1.250,00, caclcue 
um aumento de 10%.
Para os inferiores ou iguais, o aumento será
de 15%.'''
sal = float(input('Digite o salário do funcionário: '))
if sal > 1250:
    tot0 = sal * (10/100)
    tot1 = sal + tot0
    print('''
    Esse funcionário receberá um aumento de 10%.
    Assim sendo seu salário passará a ser R${:.2f}.
    '''.format(tot1))
elif sal <= 1250:
    tot0 = sal * (15/100)
    tot1 = sal + tot0
    print('''
    Esse funcionário receberá um aumento de 15%.
    Assim sendo seu salário passará a ser R${:.2f}.
    '''.format(tot1))