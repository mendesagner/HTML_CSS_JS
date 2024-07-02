import random

a1 = input('primeiro aluno: ')
a2 = input('segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('quarto aluno: ')
alunos = [a1,a2,a3,a4]

print('o aluno escolhido foi {}'.format(random.choice(alunos)))