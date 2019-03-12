# We can wrap the entire value in an int() function; 
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

other = input('Numero qualquer...')

print('A soma dos dois números é :', a + b)
print('A subtração dos dois números é :', a - b)
print('A divisão dos dois números é :', a / b)
print('A multiplicação dos dois números é :', a * b)

# Or wrap only the values
print('O número qualquer mais ele mesmo é é: ', int(other) + int(other))