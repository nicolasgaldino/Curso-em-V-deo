'''Crie um programa que çeida a idade e o sxo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer continuar ou não.
No final mostre:
A - quantas pessoas tem mais de 18 anos;
B - quantos homens foram cadastrados;
C - quantas mulheres têm menos de 20 anos;'''
tot = masc = idadeFem = 0
while True:
  idade = int(input('Idade: '))
  sexo = ' '
  while sexo not in 'MF':
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
  if idade >= 18:
    tot += 1
  if sexo == 'M':
    masc += 1
  if sexo == 'F' and idade < 20:
    idadeFem +=1
  res = ' '
  while res not in 'SN':
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if res == 'N':
    break
print(f'''
Total de pessoas com 18 anos: {tot};
Total de homens cadastrados: {masc};
Total de mulheres com menos de 20 anos: {idadeFem};
''')