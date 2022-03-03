pre = float(input('Digite o preço do produto: '))
desc = (5 * pre) / 100
tot = pre - desc
print('O preço do produto é R${} aplicando um desconto de 5% passará a custar R${:.2f}'.format(pre, tot))