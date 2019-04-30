# Exercícios Repetição usando “Enquanto” ou “while”

# a) Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.

    n = int(input('Digite um número de 1 a 10...\n'))
    i = 1

    while i <= 10:
        print('{} X {} = {}'.format(n, i, (n*i)))
        i += 1


# b) Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100).

    cont = 1
    som = 0

    while cont <= 100:
        print(cont, ' + ')
        som += cont
        cont+= 1

    print('A soma de 1 a 1000 é: {}'.format(som))

# c) Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.

    n1 = 0
    i = 1

    while i < 500:
        i += 1
        if i % 2 == 0:
            n1 += i

    print('A soma dos valores pares de 1 a 500 é: {} . '.format(n1))

# d) Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20. Para verificar se o número é ímpar, efetuar dentro da malha a verificação lógica desta condição com a instrução se, perguntando se o número é ímpar; sendo, mostre-o; não sendo, passe para o próximo passo.

    i = 0

    while i < 20:
        i+= 1
        if i % 2 != 0:
            print('Impar:', i)

# e) Apresentar os resultados das potências de 3, variando do expoente 0 até o expoente 15. Deve ser considerado que qualquer número elevado a zero é 1, e elevado a 1 é ele próprio. Observe que neste exercício não pode ser utilizado o operador de exponenciação do portuguol (^) ou python(**).

    expo = 0
    base = 3
    pot = 0

    while expo <= 15:
        
        if expo == 0:
            pot = 1
        elif expo == 1:
            pot = base
        else:
            pot *= base
        print('{} elevado a {} = {}'.format(base, expo, pot))
        expo += 1

# f) Elaborar um programa que apresente como resultado o valor de uma potência de uma base qualquer elevada a um expoente qualquer, ou seja, de BE, em que B é o valor da base e E o valor do expoente. Observe que neste exercício não pode ser utilizado o operador de exponenciação do portuguol (^).

    base = int(input('Digite a base...\n'))
    expo = int(input('Digite o exponente...\n'))

    if expo == 0:
        pot = 1
    elif expo < 0:
        base = 1 / base
        expo = -(expo)

    cont = 1
    pot = base

    while cont < expo:
        pot *= base
        cont += 1

    print('{} elevado a {} = {}'.format(base, expo, pot ))

# g) Escreva um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é formada pela seqüência: 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., etc. Esta série se caracteriza pela soma de um termo atual com o seu anterior subseqüente, para que seja formado o próximo valor da seqüência. Portanto começando com os números 1, 1 o próximo termo é 1+1=2, o próximo é 1+2=3, o próximo é 2+3=5, o próximo 3+5=8, etc.

    qnt = int(15)
    ant = 0
    seg = 1
    fibo = []
    for i in range(qnt):
    fibo.append( ant )
    ant , seg  = seg, ant + seg

    print(fibo)

# h) Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit, de 10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius. O programa deve apresentar os valores das duas temperaturas. A fórmula de conversão É F = (9C+160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

    cel = 10
    while cel <= 100:
    fah = (9 * cel + 160) / 5
    print ("Celsius=", cel, "Fahrenheit=", fah)
    cel = cel + 10

# Exercícios Repetição usando “Repita” ou “do ..while” (Não tem no python)

# 1) Apresentar os quadrados dos números inteiros de 15 a 200.

    n = 15

    while n <= 200:
    print('Quadrado de {} = {}'.format(n, n*n))
    n += 1

# 2) Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.

    n1 = 0
    i = 1

    while i < 500:
        i += 1
        if i % 2 == 0:
            n1 += i

    print('A soma dos valores pares de 1 a 500 é: {} . '.format(n1))

# 3) Apresentar todos os números divisíveis por 4 que sejam menores que 200. Para verificar se o número é divisível por 4, efetuar dentro da malha a verificação lógica desta condição com a instrução se, perguntando se o número é divisível; sendo, mostre-o; não sendo, passe para o próximo passo. A variável que controlará o contador deve ser iniciada com o valor 1.

    for cont in range(200):
    if cont % 4 == 0 and cont > 0:
        print('Divisível por 04:', cont)

# 4) Elaborar um programa que efetue o cálculo e no final apresente o somatório do número de grãos de trigo que se pode obter num tabuleiro de xadrez, obedecendo à seguinte regra: colocar um grão de trigo no primeiro quadro e nos quadros seguintes o dobro do quadro anterior. Ou seja, no primeiro quadro coloca-se 1 grão, no segundo quadro colocam-se 2 grãos (neste momento têm-se 3 grãos), no terceiro quadro colocam-se 4 grãos (tendo neste momento 7 grãos), no quarto colocam-se 8 grãos (tendo-se então 15 grãos) até atingir o sexagésimo quarto (64o) quadro. Utilize variáveis do tipo real como acumuladores.

    tab = 1
    trigo = 1
    trigo_ttl = trigo

    while tab <= 64:
    tab += 1
    trigo *= 2
    trigo_ttl += trigo

    print('Podem ser obtidos {} grãos num tabuleiro.'.format(trigo_ttl))

# 5) Elaborar um programa que efetue a leitura de 15 valores numéricos inteiros e no final apresente o total do somatório da fatorial de cada valor lido.

    n = int(input("Digite o valor de n: "))
    fat = 1
    i = 2

    while i <= n:
        fat = fat*i
        i = i + 1

    print("O valor de {}! é = {}".format(n, fat))