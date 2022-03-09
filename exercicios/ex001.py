nome = input('Qual é o seu nome? ').strip()
idade = input('Quantos anos você tem? ').strip()
prof = input('Qual sua profissão? ').strip()
print('''
Olá {}, tudo bem?
VOcê tem {} anos, e trabalha como {}, legal!
'''.format(nome, idade, prof))