nome = input('Qual seu nome? ').strip()
dia = input('Qual a sua data de nascimento? ').strip()
mes = input('Qual seu mês de nascimento? ').strip()
ano = input('Qual seu ano de nascimento? ').strip()
print('''
Olá {}!
Pelo que você digitou, sua data de nascimento é {} de {} de {}, certo?
'''.format(nome, dia, mes, ano))