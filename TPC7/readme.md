Para TPC desta semana foi proposto criar uma motor de pesquisa e criar uma tabela ao dicionário médico.

**Motor de Pesquisa**

Para criar a pesquisa foi definido um formulário com destino para "/pesquisar_conceitos" e método GET, permitindo o envio dos dados para esse URL ao submeter o formulário. O formulário contém um campo de texto para inserir o termo de pesquisa, identificado pelo atributo "q", cujo valor é enviado com a chave "q" ao submeter o formulário. Além disso, um botão "Pesquisar" facilita a submissão do formulário. O termo de pesquisa é recebido como "q" e utilizado para procurar correspondências nos conceitos, tanto no nome quanto na descrição, ignorando diferenças de maiúsculas e minúsculas. Os resultados são apresentados na página "conceitos.html", e se nenhum resultado for encontrado, é exibida a mensagem "Nenhum resultado encontrado".

**DataTable**

Foi estabelecida uma rota em Flask para "/table", onde uma função renderiza o template "table.html", passando os conceitos como argumento. Dentro do template "table.html", uma tabela responsiva é criada com DataTables, mostrando os conceitos com os cabeçalhos "Conceito", "Descrição" e "Tradução EN". 
Além disso, um script jQuery é utilizado para inicializar o DataTables na tabela. Por fim, um link de navegação intitulado "Tabela" redireciona para "/table" quando clicado.