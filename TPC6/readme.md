O trabalho de casa era desenvolver uma aplicação Flask utilizando em conjunto Jinja2. 
O objetivo era clicar em um conceito e a aplicação abriria uma nova página contendo o conceito, a descrição e a tradução em inglês.

Para isso, foi criado três templates, para além do Parent.html.

- Parent.html:

    Contém o esqueleto da página HTML. 
    
    Criamos uma barra de navegação, com dois botões, "home" e "conceitos". Quando se pressiona conceitos, é direcionado para uma nova página. A página é definida em conceitos.html

    Colocamos um footer.

- Home(F).html: Neste template, temos o título.

- conceitos.html: Neste template, utilizando o Bootstrap, criamos uma lista com todos os conceitos.

- Designacao.html: temos os conceitos, designação e a tradução.