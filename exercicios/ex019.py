#Um professor quer sortear um de seus alunos para
'''apagar o quadro. Faça um programa que o ajuda, 
lendo o nome deles e escrevendo o nome do escolhido.
------------------------------------------------------------------'''
from random import choice
alu1  = str(input('Primeiro aluno: '))
alu2  = str(input('Segundo aluno: '))
alu3  = str(input('Terceiro aluno: '))
alu4  = str(input('Quarto aluno: '))
lista = [alu1, alu2, alu3, alu4]
print('O sorteado foi: {}.'.format(choice(lista)))