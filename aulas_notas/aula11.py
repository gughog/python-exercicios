"""

=== cores no terminal

    O padrão abaixo serve como modelo para aplicar 
cores e estilos no terminal:

    \033[style; text; background m 

Os parametros abaixo são os básicos, mas não são os 
unicos, apenas para nós iniciarmos:

== style:

    O nosso style poderá ser :

> '0' : Sem estilo algum.
> '1' : Estilo negrito.
> '4' : Sublinhado.
> '7' : Negativo.

== text:

    As formatações de cores podem ser:

> '30' : branco; 
> '31' : vermelho;
> '32' : verde;
> '33' : amarelo;
> '34' : azul;
> '35' : roxo;
> '36' : ciano;
> '37' : cinza;

== background

    As formatações de background são as mesmas das
de texto, aporém iniciam na numeração 40:

> '40' : branco; 
> '41' : vermelho;
> '42' : verde;
> '43' : amarelo;
> '44' : azul;
> '45' : roxo;
> '46' : ciano;
> '47' : cinza;


"""

sal = int(input('Digite o seu \033[32msalário\033[m...\n'))
div = int(input('Digite suas \033[31mdívidas\033[m...'))
cores = {
        'azul' : '\033[1;34m',
    'vermelho' : '\033[1;31m' 
}
# Dá para usar essa estrutura de dados chamada 
# dicionario para guardar os códigos e então chamar
# com o .format() , usando duas chaves para envolver
# o texto e escrevendo nelas o objeto e o index deste.


if div > sal:
    print('Você está no \033[1;31;40mvermelho\033[m esse mês...')
else:
    print('Você está com as contas no \033[1;34;40mazul\033[m esse mês...')