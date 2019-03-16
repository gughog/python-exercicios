# Faça um programa que leia um número de 0 a 9999 e 
# mostre na tela cada um dos dígitos separados.
# Ex.: input: 1834 , output: 
# 'unidades: 4', 'dezenas: 3', 
# 'centenas: 8', 'milhar: 1'
# Opcional: faça isso usando strings, e da forma 
# matemática.

# usando Strings:
n = str(input('Digite um valor de 0 a 9999:\n'))

print('== unidades: \n{}'.format(n[3]))
print('== dezenas: \n{}'.format(n[2]))
print('== centenas: \n{}'.format(n[1]))
print('== milhar: \n{}'.format(n[0]))
