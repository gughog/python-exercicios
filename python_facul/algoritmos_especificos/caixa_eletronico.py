# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao user o VALOR a ser sacado (inteiro), e o programa vai informar quantas cédulas de cada valor serão entregues.

print('=' * 30)
print('{:^30}'.format('BANCO GUGHOG'))
print('{:^30}'.format('Notas de R$2, R$5,'))
print('{:^30}'.format('R$10, R$20, R$50 e R$100.'))
print('=' * 30)

valor = int(input('Qual o valor você deseja sacar? R$ '))
total = valor
nota = 100
totalnotas = 0

while True:
    if total >= nota:           # Enquanto nota = 50
        total -= nota
        totalnotas += 1
    else:
        if totalnotas > 0:      # Garante que imprima apenas notas q existam
            print('Total de {} notas de R$ {}'.format(totalnotas, nota))
        if nota == 100:          # Reatribui e vai pra proxima nota
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 2
        totalnotas = 0
        if total == 0:
            break

print('=' * 30)
print('{:^30}'.format('Volte sempre ao banco GUGHOG!'))