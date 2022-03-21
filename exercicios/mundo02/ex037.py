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
    binario = bin(num)
    print('{} em Binário, fica: {}'.format(num, binario))
elif opcao == '2':
    octal = oct(num)
    print('{} em Octal, fica: {}'.format(num, octal))
elif opcao == '3':
    hexadecimal = hex(num)
    print('{} em Hexadecimal, fica: {}'.format(num, hexadecimal))