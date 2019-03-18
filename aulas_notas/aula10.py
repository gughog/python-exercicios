""" 
# Estruturas condicionais pt-01

## Estrutura básica: 


op = input('Deseja seguir? (s/n)')

if op == 's':
    print('Aguarde... Pronto!')
else:
    print('App terminado.')

## Estrutura básica 02 (Mais curta, tipo um ternário):

op = input('Deseja seguir? (s/n)')
print('Aguarde...pronto!' if op == 's' else 'App terminado.')


# Lembrar sempre :
# - identar uma vez ao entrar no bloco condicional;
# - escrever a condição e então por dois pontos, tando do if, quando do else, e do elif tbm;
# - de acordo com os testes a condição pode estar ou não entre parenteses;
# - Para uma condição "Se não... se" use o "elif";

===================================================

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

# Maneira padrão:

---------------------------------------------------
if m >= 6:
    print('Parabéns, sua média foi de {:.2f}, você passou!'.format(m))
else:
    print('Você foi reprovado com a média de {:.2f}.'.format(m))
---------------------------------------------------
# Maneira simplificada: 

print('PASSOU!' if m >= 6 else 'REPROVOU!')

---------------------------------------------------
"""

