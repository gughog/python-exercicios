"""
Desenvolva um app que pergunte a distancia de uma
viagem  em km. Calcule o preço da passagem, cobrando
R$ 0,50 por km para viagens de até 200km e R$ 0,45
para viagens mais longas.

"""
d = int(input('Digite a distância da viagem em Km...\n'))

if d <= 200:
    print('O custo total para {} Km é de R$ {:.2f} .'.format(d, (d * 0.50)))
else :
    print('O valor total para {} Km é de R$ {:.2f} .'.format(d, (d * 0.45)))