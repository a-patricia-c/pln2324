Ficha de expressões regulares 1
A ficha é sobre expressões regulares, que são padrões de pesquisa usados para corresponder ou encontrar sequências de caracteres numa string.

O exercício 1 é dividido em várias alineas. Neste exercicio é dada uma linha de texto e temos que definir um programa.
- Na alínea 1.1, defini um programa que determina se a palavra "hello" aparece no ínicio da linha. Para isso, utilizei o re.match. O match serve para determinar se a re combina com o ínicio da string.
- Na alínea 1.2, defini um programa que determina se a palavra "hello" aparece em qualquer posição da linha. Para isso, utilizei o re.search. O search procura em toda a string, procurando qualquer local onde esta RE tem correspondência.
- Na alínea 1.3, defini um programa que pesquisa por todas as ocorrências da palavra "hello". Para isso, utilizei o re.findall. O findall encontra todas as substrings onde a RE corresponde, e as retorna como uma lista.
- Na alínea 1.4, defini um programa que pesquisa por todas as ocorrências da palavra "hello" dentro da linha e substituir por "*YEP*". Para isso, utilizei o re.sub. O sub substitui padrões em uma string por um texto de substituição.
- Na alínea 1.5, defini um programa que pesquisa por todas as ocorrências do caracter vírgula e separa em linhas nesse caractere. Para isso, utilizei o re.split. O split é utilizado para dividir uma string em partes usando um padrão de expressão regular como delimitador.

Exercício 2
Defini uma função "palavra_magica" com o objetivo de procurar na frase a palavra "por favor" e um sinal de pontuação. Utilizei o re.search que procura na string completa e coloquei "por favor[.,;:!?]?$" que irá procurar pela palavra "por favor" e por um sinal de pontuação "[.,;:!?]" no final da frase "$" e o que procuro poderá aparecer ou não "?".

Exercício 3
Defini uma função "narcissismo" que calcula quantas vezes a palavra "eu" aparece na frase. Utilizei um findall que retorna numa lista então utilizei o len para saber o número de vezes que a palavra aparece. Adicionei o re.IGNORECASE, para considerar tanto maiuscula como minuscula.

Exercício 4
Defini uma função "troca_de_curso" e utilizei o re.sub que substituiu todas as ocorrências de "LEI" por "BG" na frase.

Exercício 5
Defini uma função "soma_string" que tinha como objetivo receber a *string* com vários números separados por vírgulas e devolvi a soma dos números. Utilizei o re.split e como os elementos na lista são string, transformei em números usando o *float* e no fim fiz a soma utilizando o *sum*.

Exercício 6
Defini uma função "pronomes" que encontra e devolve todos os pronomes presentes utilizando o re.findall. Adicionei o re.IGNORECASE, para considerar tanto maiuscula como minuscula.

Exercício 7
Defini uma função "variavel_valida" que recebe uma *string* e determina se é um nome válido. Utilizei o re.match para procurar no ínicio da linha, o "^" obriga que no ínicio da linha tenha uma letra "[A-Za-z]" e apenas contenha letras, números e underscores "[a-zA-Z0-9_]*$" para ser válida.

Exercício 8
Defini a função "inteiros" que devolve todos os números inteiros presentes. Utilizei o re.findall e coloquei "-?[0-9]+", considerava números positivos e negativos "-?". No entanto, não consegui arranjar uma solução que não devolvesse números decimais.

Exercício 9
Defini a função "underscores" que susbtitui os espaços por underscores. Utilizei o re.sub para substituir e adicionei "\s+" para susbtituir todos os espaços presentes apenas por um underscore.

Exercício 10
Defini a função "codigos_postais" para dividir os codigos pelo hifen utilizando re.split. O resultado desta divisão ficou na lista cp.






