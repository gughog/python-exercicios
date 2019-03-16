n = str(input('Digite o nome a ser analizado:\n'))
n1 = n.replace(' ', '')

print('== Nome em caixa alta:\n{}'.format(n.upper()))
print('== Nome em letras minusculas:\n{}'.format(n.lower()))
print('== Núm. de caracteres sem espaços:\n{}'.format(len(n1)))
print('== Núm. de letras do primeiro nome:\n{}'.format(len(n.split()[0])))