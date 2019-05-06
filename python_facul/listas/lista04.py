# Estruturas de Repetição : Para … de.. ate..faca (For in range)

# 1) Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.

    n1 = int(input('Digite um numero de 0 a 10... \n'))
    for x in range(10):
        print('{} x {} = {}'.format(n1, x+1, n1 * (x + 1)))
        x += 1

# 2) Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100)

    x1 = 0
    for x in range(101):
        x1 += x 

    print(x1)

# 3) Escreva um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é formada pela seqüência: 1, 1, 2, 3, 5, 8, 13, 21, 34, ..., etc. Esta série se caracteriza pela soma de um termo atual com o seu anterior subseqüente, para que seja formado o próximo valor da seqüência. Portanto começando com os números 1, 1 o próximo termo é 1+1=2, o próximo é 1+2=3, o próximo é 2+3=5, o próximo 3+5=8, etc.

    a = 1
    b = 0

    print(b)

    for i in range(0,15):
        c = b
        b = a
        a = c + b
        print(a)

# 4) Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit, de 10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius. O programa deve apresentar os valores das duas temperaturas. A fórmula de conversão é F = (9C+160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

    c = 10

    for i in range(0,10):
        f = ((9 * c) + 160) / 5
        print('Celsius: {}°C, Fahrenheit: {}°F '.format(c, f))
        c += 10

# 5) Elaborar um programa que apresente como resultado o valor do fatorial dos valores ímpares situados na faixa numérica de 1 a 10.

    for i in range(0,10):
        fat = 1
        x = 1
        while x <= i:
            fat *= x
            x += 1

    print('fatorial de {} = {}'.format(x, fat))