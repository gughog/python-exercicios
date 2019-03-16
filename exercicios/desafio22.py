# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# 1. O nome com todas as letras maiúsculas e minúsculas. 
# 2. Quantas letras ao todo (sem considerar espaços). 
# 3. Quantas letras tem o primeiro nome.

n = str(input('Digite o nome a ser analizado:\n'))
n1 = n.replace(' ', '')

print('== Nome em caixa alta:\n{}'.format(n.upper()))
print('== Nome em letras minusculas:\n{}'.format(n.lower()))
print('== Núm. de caracteres sem espaços:\n{}'.format(len(n1)))
print('== Núm. de letras do primeiro nome:\n{}'.format(len(n.split()[0])))