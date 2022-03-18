me = float(input('Digite uma distância em metros: '))
print('''
Você digitou {} metros que em:
decâmetro equivale a {} dam;
hectômetro equivale a {} hm;
quilômtro equivale a {} km;
decímetro equivale a {} dm;
centímetro equivale a {} cm;
milímetro equivale a {} mm;
'''.format(me, me * 10, me * 100, me * 1000, me / 10, me / 100, me / 1000))