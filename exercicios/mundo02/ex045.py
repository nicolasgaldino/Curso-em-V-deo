'''Crie um programa que faça o computador
jogar Jokenpô com você.'''
res = 'S'
while res == 'S':
    from random import choice
    lista = ['Pedra', 'Papel', 'Tesoura']
    escolha = choice(lista)
    usuario = str(input('''
    Escolha uma das opções: 
    1 - Papel
    2 - Pedra
    3 - Tesoura
    ''')).strip()
    print('''
    Computador jogou: {}
    Usuário jogou: {}
    '''.format(escolha, usuario.replace('1', 'Papel').replace('2', 'Pedra').replace('3', 'Tesoura')))
    if escolha == 'Papel':
        if usuario == '1':
            print('Empatamos, parece que grandes mentes pensam igual!')
        elif usuario == '2':
            print('Parece que ganhei mais uma meu freguês.')
        elif usuario == '3':
            print('Você venceu, mas não se acostume.')
        else:
            print('Jogada Inválida.')
    elif escolha == 'Pedra':
        if usuario == '2':
            print('Empatamos, parece que grandes mentes pensam igual!')
        elif usuario == '1':
            print('Você venceu, mas não se acostume.')
        elif usuario == '3':
            print('Parece que ganhei mais uma meu freguês.')
        else:
            print('Jogada Inválida.')
    elif escolha == 'Tesoura':
        if usuario == '3':
            print('Empatamos, parece que grandes mentes pensam igual!')
        elif usuario == '2':
            print('Você venceu, mas não se acostume.')
        elif usuario == '1':
            print('Parece que ganhei mais uma meu freguês.')
        else:
            print('Jogada Inválida.')
    res = str(input('Quer continuar? [S/N]')).upper()

