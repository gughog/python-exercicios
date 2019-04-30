# a. Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor. R:

x = int(input())
y = int(input())

if x >= y:
    print('X menos Y é igual a: {}'.format(x-y))

else:
    print('Y menos X é igual a: {}'.format(y-x))

# b.  Efetuar a leitura de um valor inteiro positivo ou negativo e apresentar o número lido como sendo um valor positivo, ou seja, o programa deverá apresentar o módulo de um número fornecido. Lembre-se de verificar se o número fornecido é menor que zero; sendo, multiplique-o por -1. R:

x = input()

if x < 0:
    print('O módulo do valor é: {}'.format((x * -1) % x ))
else:
    print('O módulo do valor é: {}'.format(x % x))

# c. Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem informando esta condição. Apresentar junto das mensagens o valor da média do aluno para qualquer condição. R:

n1 = float(input('Digite a nota 01 \n'))
n2 = float(input('Digite a nota 02 \n'))
n3 = float(input('Digite a nota 03 \n'))
n4 = float(input('Digite a nota 04 \n'))
md = (n1 + n2 + n3 + n4) / 4

if md >= 5:
    print('Passou, com a média de {} pontos!'.format(md))
else:
    print('Reprovou, com a média de {} pontos.'.format(md))

# d. Ler quatro valores referentes a quatro notas escolares de um aluno e imprimir uma mensagem dizendo que o aluno foi aprovado, se o valor da média escolar for maior ou igual a 7. Se o valor da média for menor que 7, solicitar a nota de exame, somar com o valor da média e obter nova média. Se a nova média for maior ou igual a 5, apresentar uma mensagem dizendo que o aluno foi aprovado em exame. Se o aluno não foi aprovado, indicar uma mensagem informando esta condição. Apresentar com as mensagens o valor da média do aluno, para qualquer condição. R: 

n1 = float(input('Digite a nota 01 \n'))
n2 = float(input('Digite a nota 02 \n'))
n3 = float(input('Digite a nota 03 \n'))
n4 = float(input('Digite a nota 04 \n'))
md = (n1 + n2 + n3 + n4) / 4

if md >= 5:
    print('Passou, com a media de {} pontos!'.format(md))
elif md < 7:
    nm = float(input('Digite a nota do exame...\n'))
    print('Sua nova media e de: {} pontos.'.format((md + nm) / 2))

# e. Efetuar a leitura de três valores (variáveis A, B e C) e efetuar o cálculo da equação completa de segundo grau, apresentando as duas raízes, se para os valores informados for possível efetuar o referido cálculo. Lembre-se de que a variável A deve ser diferente de zero.

# f. Efetuar a leitura de três valores (variáveis A, B e C) e apresentá-los dispostos em ordem crescente. R:

a = input('Variavel 01: \n')
b = input('Variavel 02: \n')
c = input('Variavel 03: \n')

ls = []
ls.append(a)
ls.append(b)
ls.append(c)
ls.sort()

print(ls)

# g. Efetuar a leitura de quatro números inteiros e apresentar os números que são divisíveis por 2 e 3. R:

v1 = int(input('Digite o valor 01: \n'))
v2 = int(input('Digite o valor 02: \n'))
v3 = int(input('Digite o valor 03: \n'))
v4 = int(input('Digite o valor 04: \n'))

if ((v1 % 2) == 0) and ((v1 % 3) == 0):
    print('Primeiro valor e divisivel por 2 e 3: {}'.format(v1))
    print('Dividido por 2 : {}'.format(v1 / 2))
    print('Dividido por 3 : {}'.format(v1 / 3))

if ((v2 % 2) == 0) and ((v2 % 3) == 0):
    print('Segundo valor e divisivel por 2 e 3: {}'.format(v2))
    print('Dividido por 2 : {}'.format(v2 / 2))
    print('Dividido por 3 : {}'.format(v2 / 3))

if ((v3 % 2) == 0) and ((v3 % 3) == 0):
    print('Terceiro valor e divisivel por 2 e 3: {}'.format(v3))
    print('Dividido por 2 : {}'.format(v3 / 2))
    print('Dividido por 3 : {}'.format(v3 / 3))

if ((v4 % 2) == 0) and ((v4 % 3) == 0):
    print('Quarto valor e divisivel por 2 e 3: {}'.format(v4))
    print('Dividido por 2 : {}'.format(v4 / 2))
    print('Dividido por 3 : {}'.format(v4 / 3))
 
# h. Efetuar a leitura de cinco números inteiros e identificar o maior e o menor valores. R:

n1 = int(input('Digite o valor 01: \n'))
n2 = int(input('Digite o valor 02: \n'))
n3 = int(input('Digite o valor 03: \n'))
n4 = int(input('Digite o valor 04: \n'))
n5 = int(input('Digite o valor 05: \n'))
ls = []

ls.append(n1)
ls.append(n2)
ls.append(n3)
ls.append(n4)
ls.append(n5)

ls.sort()

print('Maior valor: {}'.format(ls[4]))
print('Menor valor: {}'.format(ls[0]))
 
# i. Elaborar um programa que efetue a leitura de um número inteiro e apresentar uma mensagem informando se o número é par ou ímpar. R:

n = int(input('Informe um número... \n'))

if n % 2 == 0:
    print('O número é par.')
else:
    print('O número é impar.')

# j. Elaborar um programa que efetue a leitura de um valor que esteja entre a faixa de 1 a 9. Após a leitura do valor fornecido pelo usuário, o programa deverá indicar uma de duas mensagens: "O valor está na faixa permitida", caso o usuário forneça o valor nesta faixa, ou a mensagem "O valor está fora da faixa permitida", caso o usuário forneça valores menores que 1 ou maiores que 9. R:

n = int(input('Digite um valor... \n'))

if n >= 1 and n <= 9:
    print('O valor está na faixa permitida.')
else:
    print('O valor está fora da faixa permitida.') 

# k. Elaborar um programa que efetue a leitura de um determinado valor inteiro, e efetue a sua apresentação, caso o valor não seja maior que três. R:

n = int(input('Digite um valor...\n'))

if n <= 3:
    print('Seu valor: {}'.format(n))

# l. Elaborar um programa que efetue a leitura do nome e do sexo de uma pessoa, apresentando com saída uma das seguintes mensagens: "Ilmo Sr.", se o sexo informado como masculino, ou a mensagem "Ilma Sra.", para o sexo informado como feminino. Apresente também junto da mensagem de saudação o nome previamente informado. R:

n = input('Digite seu nome: \n')
s = input('Digite seu sexo (h/m): \n')

if s == 'h':
    print('Ilmo Sr. {}'.format(n))
elif s == 'm':
    print('Ilma Sra. {}'.format(n))
else:
    print('Erro, verifique os valores novamente.')