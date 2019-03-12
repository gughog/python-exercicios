# Operadores aritméticos


# Ordem de precedência


# Customizando o 'print()'

# Podemos usar alguns modificadores dentro das máscaras das 
# strings, quando as usamos para chamar variáveis dentro de 
# strings:


# Alinhando, por exemplo, 20 caracteres a esquerda:
""" 
n1 = input('digite seu nome: ')
print('Olá {:20}, tudo bem?'.format(n1))

OU

n1 = input('digite seu nome: ')
print('Olá {:<20}, tudo bem?'.format(n1))

"""

# Alinhando a direita:
""" 
n1 = input('digite seu nome: ')
print('Olá {:>20}, tudo bem?'.format(n1))
"""

# Centralizando a string dentro dos 20 caracteres:
""" 
n1 = input('digite seu nome: ')
print('Olá {:^20}, tudo bem?'.format(n1))

"""

# Centralizar a string entre algum caractere repetido x vezes, como por exemplo o '=':
""" 
n1 = input('digite seu nome: ')
print('Olá {:=^20}, tudo bem?'.format(n1))

"""

# Formatar um número flutuante em x casas:
""" 
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
m = n1 * n2
# O de baixo será formatado para ter apenas 3 casas flutuantes:
d = n1 / n2

print('A soma entre os números é {}, a multiplicação é {} e a divisão é {:.2f}.'.format(s, m, d))
"""

# Unir na mesma linha dois 'print()' para evitar quebra de linha:
""" 
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2

# usamos o end='' para sinalizar que a linha não terminará ali.
print('A soma entre os números é {}, '.format(s), end='')
print('a multiplicação é {}, '.format(m), end='')
print('e a divisão é {:.2f}.'.format(d))
"""

# Aplicar quebras de linha dentro de uma string:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2

# utilizamos o '\n' para realizar as quebras de linha:
print('A soma entre os números é {}, \n a multiplicação é {} \n e a divisão é {}.'.format(s, m, d))