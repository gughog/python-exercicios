# Faça um programa que leia um ano qualquer e
# mostre se ele é BISSEXTO.

a = int(input('Digite um ano qualquer...\n'))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Esse ano é BISSEXTO!')
else: 
    print('Esse ano NÃO É BISSEXTO!')