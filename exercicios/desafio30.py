# Crie um programa que leia um número e mostre na 
# tela se ele é PAR ou IMPAR.

n = int(input('Digite um número...'))

if n % 2 == 0:
    print('Este número é PAR.')
else :
    print('Este número é IMPAR.')
  
# Usando condicional simplificado:
# print('O número é PAR.' if n % 2 == 0 else 'O número é IMPAR.')