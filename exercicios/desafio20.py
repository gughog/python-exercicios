# O mesmo professor do exercicio anterior agora 
# precisa sortear a ordem de aprensentação do trabalho
# que este tinha passado. Faça um app para ajuda-lo.

from random import shuffle

n1 = str(input('Aluno 01: \n'))
n2 = str(input('Aluno 02: \n'))
n3 = str(input('Aluno 03: \n'))
n4 = str(input('Aluno 04: \n'))

alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem de apresentação será:')  
print(alunos)