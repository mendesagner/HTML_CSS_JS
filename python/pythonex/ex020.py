import random

a1 = input('primeiro aluno: ')
a2 = input('segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('quarto aluno: ')
alunos = [a1,a2,a3,a4]

ordem = random.sample(alunos,4)
print('a sequencia foi {}'.format(ordem))

#ou random.shuffle('lista') mas o shuffle embaralha a lista original, fazendo com que vc perca a ordem inicial