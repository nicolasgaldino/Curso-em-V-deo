val = input('Digite algo: ').strip()
print('''
O tipo primitivo deste valor é: {};
Só tem espaços? {};
É um número? {};
Tem apenas caracteres alfabéticos? {};
Tem apenas caracteres alfanuméricos? {};
Está em maiúsculas? {};
Está em minúsculas? {};
Está capitalizada? {};
'''.format(type(val), val.isspace(), val.isnumeric(), val.isalpha(), val.isalnum(), val.isupper(), val.islower(), val.istitle()))