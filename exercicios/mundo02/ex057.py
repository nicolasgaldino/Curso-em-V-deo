'''Faça um programa que leio o sexo
de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto.'''
res = 'S'
while res == 'S':
    sexo = str(input('''
    F - Feminino
    M - Masculino
    ''')).upper()
    if sexo != 'F' and sexo != 'M':
        print('Por favor, digite uma opção válida.')
    else:
        res = str(input('Quer continuar? [S/N]')).upper()
