n1 = int(input('Digite o primeiro valor...\n'))
n2 = int(input('Digite o segundo valor...\n'))
op = input('Digite o tipo de operação (som, sub)')

if op == 'som':
  print('O resultado da soma entre {} e {} é: {}.'.format(n1, n2, n1+n2))
if op == 'sub':
  print('O resultado da subtração entre {} e {} é: {}.'.format(n1, n2, n1-n2))

cont = input('Deseja fazer mais um calculo? (s/n)')

while cont == 's':
  n1 = int(input('Digite o primeiro valor...\n'))
  n2 = int(input('Digite o segundo valor...\n'))
  op = input('Digite o tipo de operação (som, sub)')

  if op == 'som':
    print('O resultado da soma entre {} e {} é: {}.'.format(n1, n2, n1+n2))
  if op == 'sub':
    print('O resultado da subtração entre {} e {} é: {}.'.format(n1, n2, n1-n2))

  cont = input('Deseja fazer mais um calculo? (s/n)\n')

print('==== Fim da aplicação =====')
