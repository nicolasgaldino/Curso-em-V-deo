re = float(input('Carteira: R$'))
do = re / 5.10 #para este exemplo estou considerando o dólar a R$3.27
print('Você tem R${:.2f}, com esse valor você pode comprar US${:.2f}.'.format(re, do))