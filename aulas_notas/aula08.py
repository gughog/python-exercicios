# Módulos

# Para importar libs e módulos no python usamos a palavra 
# reservada 'import' seguida do módulo que estamos importando:

"""

import math

"""

# Caso precisássemos importar somente um componente de um dado
# módulo, utilizaríamos a seguinte sintaxe:

"""

from math import ceil

Ou mais de uma:

from math import ceil, floor, pow

"""

# ========================================================
""" 

import math
n = int(input('Digite um número: \n'))
rq = math.sqrt(n)

print('A raíz quadrada de {} é igual a {}'.format(n, math.ceil(rq)))

========================================================

from math import ceil

n = float(input('Digite um número real: '))
print('Arredondando para cima teremos {}.'.format(ceil(n)))

========================================================
"""
# ========================================================
""" Usando o módulo random:  

import random

n = random.random()
print(n)

"""
""" Utilizando o randint, para obter números aleatórios entre um dado intervalo:

import random 
n = random.randint(1, 25)
print(n)

"""
# ========================================================

import p