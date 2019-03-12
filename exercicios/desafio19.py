# Faça um app em python que sorteie um aluno entre 4
# para que o professor possa escolher quem irá apagar
# o quadro da sala.

from random import choice

n1 = str(input('Digite o primeiro nome:\n'))
n2 = str(input('Digite o segundo nome: \n'))
n3 = str(input('Digite o terceiro nome: \n'))
n4 = str(input('Digite o quarto nome: \n'))
alunos = [n1, n2, n3, n4]

print('O aluno selecionado foi: {}'.format(choice(alunos)))