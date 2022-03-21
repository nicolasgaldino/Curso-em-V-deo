'''Desenvolva uma lógica que leia o peso e altura de
uma pessoa, calcule seu IMC e mostre seu status de 
acordo com a tabela abaixo:
- Abaixo de 18.4: Abaixo do peso
- Entre 18.5 e 24.9: Pesoa Ideal
- 25 até 29.9: Sobrepeso
- Acima de 30: Obesidade
- Maior que 40: Obesidade Grave'''
#IMC = Peso ÷ (Altura × Altura)
nome = str(input('Informe seu nome: '))
altura = float(input('Informe sua altura(m e cm): '))
peso = float(input('Informe seu peso(Kg): '))
imc = peso / (altura * altura)
if imc < 18.4:
    print('Olá {}! Seu peso atual é {}Kg, você está abaixo do peso ideal.'.format(nome, peso))
elif imc == 18.5 or imc <= 24.9:
    print('Olá {}! Seu peso atual é {}Kg, você no seu peso ideal.'.format(nome, peso))
elif imc == 25 or imc <= 29.9:
    print('Olá {}! Seu peso atual é {}Kg, você está com sobrepeso.'.format(nome, peso))
elif imc > 30:
    print('Olá {}! Seu peso atual é {}Kg, você está obeso(a)'.format(nome, peso))
elif imc > 40:
    print('Olá {}! Seu peso atual é {}Kg, você está com obesidade grave.'.format(nome, peso))