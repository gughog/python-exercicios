# Manipulando textos

# ==fatiamento de strings

#Isto irá pegar apenas os caracteres do indice 13 até o indice 19, tipo como numa array.
""" 
p = str('Olá meu caro watson!')
print(p[13:19])

"""

#formas de fatiamentos:
print('======= fatiamento =======')

frase = str('Oi eu sou o goku!')
frase2 = str('   Vermes insolentes  ')

print(frase)
print(frase[0:19:2]) # Isto faz com que seja printado  do indice 0 ao 19, pulando 2 caracteres por vez.
print(frase[:10]) # Isto printa os caracteres até o indice especificado.
print(frase[10:]) # Isto printa do caractere de indice 15 até o fim da string.
print(frase[9::2]) # Isto printará do 9 até o final, ja que não foi especificado, pulando 2 caracteres por vez.

# ==análise de strings
print('======= análise de strings =======')

print(len(frase)) # calcula o comprimento da string, no caso 18 caracteres.
print(frase.count('o')) # conta quantas vezes um caractere definido se repete dentro da string.
print(frase.count('o', 0, 9)) # contagem da repetição de caracteres junto do fatiamento da string, considerando apenas do 0 ao 9.
print(frase.find('goku')) # Procura na string o caractere ou a sequencia passada na string em questão, retornando onde esta inicia. Retorna -1 se ela não existir.
print(frase.find('kakaroto')) # 'kakaroto' não existe nesta string, por isso retornou '-1'.
print('goku' in frase) # Utilizando o in analizamos se uma string existe em (ou 'in') uma lista (array), retornando um booleano ao invés da posição do caractere.

# ==transformação
print('======= Transformação de strings =======')

print(frase.replace('goku', 'vegeta')) # Substitui um pedaço da string, por outro.
print(frase.upper()) # transforma o texto para caixa alta.
print(frase.lower()) # transforma o texto para minusculas.
print(frase.capitalize())  # capitaliza (poe a primeira letra da frase) em caixa alta.
print(frase.title()) # deixa maiuscula toda primeira letra de cada palavra da string.

print(len(frase2))
print(frase2)
print(frase2.strip())
print(frase2.rstrip()) 
print(frase2.lstrip()) 
