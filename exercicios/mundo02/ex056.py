'''Desenvolva um programa que leia o
nome, idade e sexo de 4 pessoas.
No final do programa mostre:
- A média de idade do grupo;
- Qual é o nome do homem mais velho;
= Quantas mulheres têm menos de 21 anos;'''
totIdade = 0
medIdade = 0
idadeHom = 0
nomVelh = ''
mulhVin = 0
for c in range(1, 5):
    print('Pessoa {}.'.format(c))
    nome = str(input('Digite um nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    totIdade = totIdade + idade
    if c == 1 and sexo == 'M':
        idadeHom = idade
        nomVelh = nome
    if sexo == 'M' and idade > idadeHom:
        idadeHom = idade
        nomVelh = nome
    if sexo == 'F' and idade < 20:
        mulhVin = mulhVin + 1
medIdade = totIdade / 4
print('''
    A média de idade do grupo é {:.1f} anos;
    O homem mais velho tem {} anos e se chama {};
    Ao todos são {} mulher com menos de 20 anos;
    '''.format(medIdade, idadeHom, nomVelh, mulhVin))