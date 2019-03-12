# faça um app que leia um numero inteiro e mostre na tela o 
# seu sucessor e seu antecessor.

num = int(input('Digite algum número: '))

print('Você digitou o número {},\n cujo o sucessor é {}\n e o antecessor é {}.'.format(num, num + 1, num - 1))