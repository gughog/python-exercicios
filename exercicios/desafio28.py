# Escreva um programa que faça o computador "pensar"
# em um número inteiro entre o e 5 e peça para o 
# usuário tentar descobrir qual foi o número escolhido
# pelo computador. O programa deverá escrever na tela
# se o usuário ganhou ou perdeu.

from random import randint
cn = randint(1,5)
print('== Tente adivinhar qual o número que o pc escolheu! ==')
pn = int(input('Digite um número de 1 a 5...\n'))

if pn == cn :
    print('Você acertou!')
else: 
    print('Você perdeu, tente novamente!')