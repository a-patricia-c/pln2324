**TPC3**

Neste trabalho, converteu-se o pdf "dicionário médico", fornecido pelo docente, em text. De seguida, processou-se o texto utilizando expressões regulares.

**Data cleaning**

Efectou-se a limpeza de dados ao retirar as quebras de páginas '\n?\f' do texto. 

**Marcar designações**

Cada vez que houve '\n\n' indicava que era uma designação e adicionou-se o @ para identificar, utilizando o "sub".

**Capturar termos**

'@(.+)\n([^@]+)' é utilizado para capturar termos que começam com @ e são seguidos por quaisquer caracteres até uma nova linha (\n), seguidos pela explicação, que é tudo exceto @, utilizando o findall.

**HTML**

Após o tratamento do texto, utilizou-se o HTML para criar uma página. 
Definiu-se o título "Dicionário Médico", a descrição "Dicionário médico ddesenvolvido na disciplina de PLNEB" e as prioridades respetivas (cor da letra, cor do fundo, entre outras).
Por fim, definiu-se o body, que representava os termos.
Juntou-se as três variáveis para formar o HTML, que é visualizado na "aula3.html".

**Desafios e dificuldades no TPC3**

No processamento do texto, as minhas modificações não foram suficientes para corrigir o texto por completo, no entanto consegui alcançar um texto composto.
O Dicionário do Médico é feito com HTML básico porque não tenho muita experiência a trabalhar com isto, no entanto, foi interessante e fiquei entusiamada em trabalhar futuramente.
