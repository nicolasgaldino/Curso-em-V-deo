'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final mostre:
A - qual é o total gasto na comprar;
B - quantos produtos custam mais de R$1000;
C - qual é o nome do produto mais barato;'''
tot = maior = menor = cont = 0
prodBarat = ''
while True:
  produto = str(input('Nome do produto: ')).strip()
  preco = float(input(f'Preço do {produto}: R$'))
  cont += 1
  tot += preco
  if preco > 1000:
    maior += 1
  if cont == 1:
    menor = preco
    prodBarat = produto
  else:
    if preco < menor:
      menor = preco
      prodBarat = produto
  res = ' '
  while res not in 'SN':
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if res == 'N':
    break
print(f'''
O total da compra foi: R${tot:.2f};
Quantidade de produtos acima de R$1.000: {maior};
O produto mais barato foi {prodBarat}, que custou: R${menor:.2f};
''')