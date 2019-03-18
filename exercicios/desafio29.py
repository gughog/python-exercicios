# Escreva um programa que leia a velocidade de um 
# carro. Se ele ultrapassar 80km/h, mostre uma msg
# dizendo que ele foi multado. A multa será de 
# R$ 7,00 por km acima do limite.

v = int(input('Digite sua velocidade atual... \n'))
vmax = int(80)
mul = int(7)

if v > vmax :
    print('Você está acima do limite de velocidade!')
    print('Você foi multado em R$ {} .'.format((v - vmax) * mul))
else :
    print('Você está dentro do limite máx permitido. Continue assim!')

