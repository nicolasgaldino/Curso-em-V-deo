'''Escreva um programa que leia um número
inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 - binário;
2 - octal;
3 - hexadecimal;'''
num = int(input('Digite um valor inteiro: '))
opcao = str(input('''
Digite uma opção para a conversão do valor {}.
1 - Binário;
2 - Octal;
3 - Hexadecimal;
'''.format(num))).strip()
if opcao == '1':
    binario = format(num, 'b')
    print('{} em Binário, fica: {}'.format(num, binario))
elif opcao == '2':
    octal = format(num, 'o')
    print('{} em Octal, fica: {}'.format(num, octal))
elif opcao == '3':
    hexadecimal = format(num, 'x')
    print('{} em Hexadecimal, fica: {}'.format(num, hexadecimal))
else:
    print('Opção inválida, tente novamente.')