#---------------------------------------------------------------------
for c in range(1, 10):
    print(c)
print('FIM!')
#---------------------------------------------------------------------
c = 1
while c < 10:
    print(c)
    c = c + 1
print("FIM!")
#---------------------------------------------------------------------
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM!')
#---------------------------------------------------------------------
res = 'S'
while res == 'S':
    n = int(input('Digite um valor: '))
    res = str(input('Quer continuar? [S/N]')).upper()
print('FIM!')
#---------------------------------------------------------------------
num = 1
while num != 0:
    num = int(input('Digite um valor: '))
print('FIM!')
#---------------------------------------------------------------------
num = 1
par = 0
imp = 0
print('Para encerrar o programa digite: 0')
while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            imp += 1
print('''
{} são números pares;
{} são números ímpares;
'''.format(par,imp))
print('FIM!')
#---------------------------------------------------------------------
idade = 1
cont = 0
listIdade = [cont]
print('Para encerrar o programa digite: 0')
while idade != 0:
    idade = int(input('Informe sua idade: '))
    listIdade[0] += 1
    cont += 1
print(listIdade)
print('FIM!')
#---------------------------------------------------------------------