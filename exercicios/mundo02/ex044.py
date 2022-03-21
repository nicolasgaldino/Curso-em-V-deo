'''Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e
condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto;
- À vista no cartão: 5% de desconto;
- Em até 2x no cartão: preço normal;
- 3x ou mais no cartão: 20% de juros;'''
produto = str(input('Qual produto você está comprando? ')).lower().strip()
preco = float(input('Qual o valor do {}? R$ '.format(produto)))
opcao = str(input('''
Escolha uma forma de pagamento para o {}:
1 - À vista no dinheiro ou cheque 10% de desconto;
2 - À vista no cartão 5% de desconto;
3 - Até 2x no cartão preço normal;
4 - Até 3x no cartão 20% de juros;
'''.format(produto))).strip()
if opcao == '1':
    tot = preco * (10 / 100)
    res = preco - tot
    print('À vista no dinheiro ou chueque o {}, ficará R${:.2f}.'.format(produto, res))
elif opcao == '2':
    tot = preco * (5 / 100)
    res = preco - tot
    print('À vista no cartão o {}, ficará R${:.2f}.'.format(produto, res))
elif opcao == '3':
    tot = preco / 2
    print('Parcelando 2x no cartão o {}, não receberá desconto. Valor das parcelas R${:.2f}'.format(produto, tot))
elif opcao == '4':
    tot = preco * (20 / 100)
    res = preco + tot
    parcela = res / 3
    print('''
    Parcelando 3x no cartão o {}, terá 20% de acréscimo no valor final R${:.2f}.
    Valor das parcelas R${:.2f}.
    '''.format(produto, res, parcela))