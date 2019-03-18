# Faça um programa que leia um número de 0 a 9999 e 
# mostre na tela cada um dos dígitos separados.
# Ex.: input: 1834 , output: 
# 'unidades: 4', 'dezenas: 3', 
# 'centenas: 8', 'milhar: 1'
n = int(input('Digite um número de 0 a 9999...'))
nu = n // 1 % 10 # 1234 // 1 = 1234 , 1234 % 10 = 123.4 ; mod: 4
nd = n // 10 % 10 # 1234 // 10 = 123,4 (div int: 123) , 123 % 10 = 12,3 ; mod: 3
nc = n // 100 % 10 # 1234 // 100 = 12.34 (div int: 12) , 12 % 10 = 1,2 ; mod: 2
nm = n // 1000 % 10 # 1234 // 1000 = 1,234 (div int: 1) , 1 % 10 = 0,1 ; mod 1

print('Analizando o número {} temos... '.format(n))
print('Unidades: {}'.format(nu))
print('Dezenas: {}'.format(nd))
print('Centenas: {}'.format(nc))
print('Milhares: {}'.format(nm))