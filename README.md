# Portal Professor
## _Aplicação web para cadastro de professores_


Portal Professor é uma aplicação web desenvolvida na matéria Programação Web da FATEC Indaiatuba.
Essa aplicação foi desenvolvida utilziando o framework Django.

- Django
- HTML
- CSS
- JS

## Caracteristicas

- Formulário simples para cadastro de professores
- Os dados são salvos no banco de dados sqlite, podenendo ser gerenciado pelo Django Admin
- Listagem de professores
- Edição e exclusão de cadastro

## Requisitos

- Python (https://www.python.org/)
- pip (https://pypi.org/project/pip/)
- Django (https://www.djangoproject.com/)
- Crispy_forms (https://django-crispy-forms.readthedocs.io/en/latest

## Instalação

Após fazer o clone do prjeto, será necessário rodar os seguintes comandos: 
```sh
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```

Feito isso, a aplicação será exibida no navegador.

No cabeçalho encontram-se todas as funcionalidades que são:
- Listar
- Adicionar

![Home Page](https://raw.githubusercontent.com/RamonTadeuGoncalves/devDjango_portalProfessor/master/templates/static/media/home_page.png?token=GHSAT0AAAAAABWBD4B34N5I53SFIDVW4VBIYWEHNDQ)


Ao clicar em Adicionar, o formulário para cadastro do professor será exibido.

![Create New Register](https://raw.githubusercontent.com/RamonTadeuGoncalves/devDjango_portalProfessor/master/templates/static/media/create_new_register_page.png?token=GHSAT0AAAAAABWBD4B3A3WY4ZVL4GGY57N2YWEHSVQ)

Ao clicar em Listar, a lista com todos os cadastros salvos no banco de dados será exibida.
Para exibir os dados do respectivo professor, o usuário deve clicar sobre o nome do mesmo.

![List Page](https://raw.githubusercontent.com/RamonTadeuGoncalves/devDjango_portalProfessor/master/templates/static/media/list_page.png?token=GHSAT0AAAAAABWBD4B27LUDPOMOQHNP4Y46YWEHT2A)

A tela com os detalhes do cadastro é exibida.
![Detail Page](https://raw.githubusercontent.com/RamonTadeuGoncalves/devDjango_portalProfessor/master/templates/static/media/detail_page.png?token=GHSAT0AAAAAABWBD4B2QUX5JRSOW5ADXTQMYWEHV5A)

Na tela de detalhes, o usuário terá as opções para Excluir ou Editar o respectivo cadastro.
Se o usuário clicar em Excluir, o respectivo cadastro será apagado do banco de dados.
Caso o usuário clique em Editar, o formulário com os dados que foram preenchidos são exibidos em tela para serem alterados.
![Edit Page](https://raw.githubusercontent.com/RamonTadeuGoncalves/devDjango_portalProfessor/master/templates/static/media/edit_page.png?token=GHSAT0AAAAAABWBD4B2HAQR4NRCFLX2CU6MYWEHYCA)

O botão Home retorna para a página inicial do sistema.
![Home Page](https://raw.githubusercontent.com/RamonTadeuGoncalves/devDjango_portalProfessor/master/templates/static/media/home_page.png?token=GHSAT0AAAAAABWBD4B34N5I53SFIDVW4VBIYWEHNDQ)

