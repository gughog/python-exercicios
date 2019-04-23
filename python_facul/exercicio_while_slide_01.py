# 1) Apresentar os quadrados dos números inteiros de 15 a 200:

n1 = int(15)

print('Quadrado de {} é: {}.\n'.format(n1, n1*n1))

while(n1 < 200):
  n1 += 1
  print('Quadrado de {} é: {}.\n'.format(n1, n1*n1))

print('=== End ===')
