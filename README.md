# Bookstore 
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/jgmartinss/bookstore/blob/master/LICENSE)
> Bookstore é um projeto para colocar em prática meus conhecimentos sobre Django. Buscando explorar todos os seus recursos. 

## Objetivo
Criar uma livraria com todos o recursos de um e-commerce.
##### Funcionalidades
- Login/Logout
- Usuário pode editar informações pessoais para efetuar suas compras:
- Visualizar seus pedidos e rastrear seu produto. 
- Módulo accounts:
    - Cadastro de Usuários (informações pessoais) e Endereços.
- Módulo catalog:
    - Cadastro de Livros, Autores, Editoras, Categorias, Thumbnails e Avaliações de Usuários.
- Módulo coupons:
    - Cadastro de coupons de desconto.
- Módulo orders:
    - Controlar e visualizar pedidos e seus respectivos itens.
- Módulo newsletter:
    - Usuário poderá cadastrar multiplos emails para receber Boletins de Notícias.
- Módulo checkout:
    - Controlar os produtos no carinho, aplicando desconto e realizando cotação de entrega.
- Módulos Payments, Shipping, Sites e Summarys:
    - Em desenvolvimento.
- Interface em português.

## Dependências

- [Python](https://www.python.org/downloads/) - Versão 3.6.6+
- [Django](http://www.djangoproject.com) - 2.0
- PIPENV
- Virtualenv - 16.1.0+

## Instalação:

1. Clone o repositório:
    ```bash
    git clone https://github.com/jgmartinss/bookstore.git bookstore
    ```
1. Instalar dependências e criando ambiente:

    ```bash
    cd bookstore
    pipenv --python 3.6
    pipenv shell
    pipenv install
    pipenv install -d
    ```
3. Gere um `.env` local

    ```bash
    python contrib/env_gen.py dev
    ```


4. Sincronize a base de dados:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Crie um usuário (Administrador do sistema):

    ```bash
    python manage.py createsuperuser
    ```
6. Gerando dados randômicos (`opcional`)
    ```bash
    make populate_db
    ```
7. Teste a instalação na url http://127.0.0.1:8000 no navegador):

    ```bash
    python manage.py runserver
    ```
## Rodando testes:

1. Testes do `Django`

    ```bash
    python manage.py test
    ```
2. Testes de cobertura usando `Tox`

    ```bash
    $ tox
    visualizando coverage report $ firefox htmlcov/index.html
    ```
