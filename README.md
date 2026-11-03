 <div align="center">

# Educa Drones

### Tecnologia, educação e robótica aérea transformando o aprendizado.

**Plataforma web institucional do projeto Educa Drones, desenvolvido no IF Baiano — Campus Guanambi.**

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Framework-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/HTML5-Estrutura-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-Estilização-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-Interatividade-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
[![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-blue?style=flat-square)](#)

[Visão geral](#visão-geral) · [Funcionalidades](#funcionalidades) · [Tecnologias](#tecnologias) · [Arquitetura](#arquitetura-do-projeto) · [Estrutura](#estrutura-de-diretórios) · [Como executar](#como-executar) 

</div>

---

## Visão geral

O **Educa Drones** é um projeto de educação tecnológica e robótica aérea vinculado ao Instituto Federal Baiano (IF Baiano), Campus Guanambi.

A plataforma web foi desenvolvida para apresentar institucionalmente o projeto, divulgar suas atividades, registrar conquistas, apresentar integrantes e disponibilizar informações sobre suas iniciativas educacionais.

Mais do que um site institucional, a aplicação reúne funcionalidades de gerenciamento de conteúdo e interação com visitantes, permitindo que informações sobre o projeto sejam atualizadas por meio do painel administrativo do Django.

O desenvolvimento utiliza uma arquitetura baseada em aplicações Django, com separação entre funcionalidades, modelos, formulários, visualizações e templates.

## Funcionalidades

| Recurso | Descrição |
| --- | --- |
| **Página inicial** | Apresentação institucional do Educa Drones, com seções sobre o projeto, suas atividades e conquistas. |
| **Sobre o projeto** | Página dedicada à história, trajetória e identidade do Educa Drones. |
| **Integrantes** | Apresentação da equipe e de seus participantes. |
| **Notícias e eventos** | Exibição de publicações cadastradas no sistema, com categorias, datas, imagens e resumos. |
| **Detalhamento de notícias** | Página individual para cada publicação, acessada por meio de seu slug. |
| **Gerenciamento de conteúdo** | Cadastro e administração de notícias e conquistas por meio do Django Admin. |
| **OBaDrones** | Página institucional dedicada à Olimpíada Baiana de Drones. |
| **Linha Colibri** | Apresentação dos modelos e informações sobre o drone educacional Colibri. |
| **Livro de visitas** | Formulário para registro de visitantes e suas informações. |
| **Mapa de impacto** | Visualização geográfica dos registros de visitantes, com dados agregados por cidade. |
| **Formulário de contato** | Recebimento e processamento de mensagens enviadas pelo formulário de contato. |

## Seções do site

A plataforma está organizada em páginas independentes, integradas por meio de um layout compartilhado.

1. **Início:** apresentação do projeto, histórico, conquistas, notícias, OBaDrones, Colibri e mapa de impacto.
2. **Sobre:** trajetória e história do Educa Drones.
3. **Integrantes:** apresentação dos membros da equipe.
4. **Notícias e Eventos:** publicações e acontecimentos relacionados ao projeto.
5. **Detalhes da notícia:** conteúdo completo de cada publicação.
6. **OBaDrones:** informações sobre a Olimpíada Baiana de Drones.
7. **Colibri:** apresentação da linha de drones educacionais desenvolvida pelo projeto.
8. **Livro de visitas:** registro de visitantes e participação institucional.

## Tecnologias

### Backend

- **Python:** linguagem utilizada no desenvolvimento da aplicação.
- **Django:** framework responsável pela estrutura da aplicação, roteamento, processamento de requisições, modelos, formulários e painel administrativo.
- **Django ORM:** gerenciamento e consulta dos dados por meio dos modelos.

### Frontend

- **HTML5:** estruturação das páginas utilizando templates Django.
- **CSS3:** estilização e organização visual das interfaces.
- **JavaScript:** implementação de funcionalidades interativas.
- **Bootstrap 5.3.8:** utilizado na interface do formulário do livro de visitas.
- **Google Fonts:** carregamento da família tipográfica Poppins.

### Recursos complementares

- **Leaflet:** utilizado na implementação do mapa de impacto.
- **Canvas API:** utilizado na apresentação visual da animação da linha Colibri.
- **Geocodificação:** processo de associação de cidades a coordenadas geográficas.
- **Git e GitHub:** versionamento e hospedagem do código-fonte.

## Arquitetura do projeto

A aplicação utiliza uma estrutura modular do Django, separando responsabilidades em aplicações independentes.

### Aplicação principal — `EducaDronesWeb`

Responsável pelas configurações gerais do projeto e pela inicialização da aplicação.

Arquivos principais:

| Arquivo | Responsabilidade |
| --- | --- |
| `settings.py` | Configurações gerais do Django. |
| `urls.py` | Roteamento principal da aplicação. |
| `asgi.py` | Ponto de entrada ASGI. |
| `wsgi.py` | Ponto de entrada WSGI. |

### Aplicação — `website`

Responsável pelas páginas institucionais e pela apresentação dos conteúdos do site.

Entre suas responsabilidades estão:

- Renderização da página inicial.
- Exibição da página sobre o projeto.
- Apresentação dos integrantes.
- Listagem de notícias.
- Exibição individual de notícias.
- Páginas da OBaDrones e da linha Colibri.
- Integração dos conteúdos dinâmicos com os templates.

### Aplicação — `noticias`

Responsável pelo gerenciamento das publicações e conquistas do projeto.

O modelo `Noticia` contém os seguintes campos identificados:

| Campo | Descrição |
| --- | --- |
| `titulo` | Título da publicação. |
| `slug` | Identificador utilizado na URL. |
| `categoria` | Categoria da publicação. |
| `data_publicacao` | Data de publicação. |
| `imagem` | Imagem associada à publicação. |
| `resumo` | Resumo do conteúdo. |
| `conteudo` | Conteúdo completo da publicação. |
| `destaque_home` | Define se a publicação será exibida na área de notícias em destaque. |
| `conquista_destaque` | Define se a publicação será apresentada na seção de conquistas. |

**Funcionamento dos destaques**

A página inicial realiza consultas específicas ao banco de dados:

- Notícias em destaque: registros com `destaque_home=True`, limitados aos três primeiros resultados.
- Conquistas em destaque: registros com `conquista_destaque=True`, limitados aos quatro primeiros resultados.

A página de notícias também utiliza o campo `destaque_home` para selecionar as publicações exibidas.

O detalhamento de cada publicação utiliza o `slug` para localizar o registro correspondente. Caso não exista uma publicação com o identificador informado, o Django retorna uma resposta 404.

### Aplicação — `livro_de_visitas`

Responsável pelo registro e gerenciamento dos visitantes da plataforma.

A aplicação possui:

- Modelos para armazenamento dos registros de visitantes.
- Formulários para coleta das informações.
- Views responsáveis pelo processamento das requisições.
- Rotas próprias.
- Painel administrativo.
- Migrações para evolução da estrutura do banco de dados.
- Comando personalizado para geocodificação de cidades.

Também existe o modelo `CidadeCoordenadas`, utilizado no armazenamento de informações geográficas associadas às cidades.

O projeto possui um comando de gerenciamento chamado `geocodificar_cidades`, localizado em:

`livro_de_visitas/management/commands/geocodificar_cidades.py`

### Aplicação — `emails`

Responsável pelo processamento dos formulários relacionados ao contato.

Sua estrutura contém:

- `models.py`: definição dos modelos.
- `forms.py`: definição do formulário `Contato`.
- `views.py`: processamento das mensagens enviadas.
- `admin.py`: configuração administrativa.

O formulário de contato é integrado à página inicial por meio da aplicação `website`.

## Funcionamento das principais funcionalidades

### Notícias e conquistas

O gerenciamento de publicações é realizado por meio do modelo `Noticia`.

As informações cadastradas podem ser utilizadas em diferentes áreas da plataforma, permitindo que o conteúdo seja atualizado sem a necessidade de modificar diretamente os templates.

A seleção dos destaques é controlada por campos booleanos, permitindo separar notícias e conquistas.

### Livro de visitas e mapa de impacto

O livro de visitas permite registrar informações dos visitantes por meio de um formulário.

Os registros são processados pela aplicação `livro_de_visitas`.

A plataforma também possui uma funcionalidade de mapa de impacto, que utiliza informações geográficas para representar o alcance do projeto.

O frontend utiliza o arquivo:

`static/js/mapa-impacto.js`

O formulário de visitas possui integração com:

`static/js/formulario-cidades.js`

O comando `geocodificar_cidades` complementa essa estrutura, permitindo trabalhar com as coordenadas geográficas das cidades registradas.

### Linha Colibri

A apresentação da linha Colibri possui uma experiência visual baseada em animação de quadros durante a rolagem da página.

Os arquivos de imagem estão organizados em:

`static/img/colibri/`

O comportamento visual é controlado por:

`static/js/colibri-scroll.js`

A página utiliza um elemento Canvas para apresentar a sequência de imagens.

## Templates e componentes

O sistema utiliza o mecanismo de templates do Django para reutilização de estruturas e organização das páginas.

O arquivo `templates/layout.html` funciona como estrutura-base da aplicação.

Ele centraliza:

- Configuração HTML e metadados.
- Carregamento das fontes.
- Favicon.
- Estilos compartilhados.
- Cabeçalho.
- Área principal de conteúdo.
- Rodapé.

Os demais templates utilizam herança por meio de `{% extends 'layout.html' %}` e definem seus conteúdos nos blocos disponibilizados pelo layout.

Também existem componentes reutilizáveis:

- `components/header.html`
- `components/footer.html`
- `components/member_socials.html`

Essa organização reduz a duplicação de código e facilita a manutenção da identidade visual entre as páginas.

## Estrutura de diretórios

```text
EducaDronesWeb/
│
├── .github/
│   └── workflows/
│       └── django.yml
│
├── EducaDronesWeb/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── website/
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── noticias/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   └── migrations/
│
├── livro_de_visitas/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   ├── migrations/
│   └── management/
│       └── commands/
│           └── geocodificar_cidades.py
│
├── emails/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   └── tests.py
│
├── templates/
│   ├── layout.html
│   ├── home.html
│   │
│   ├── components/
│   │   ├── header.html
│   │   ├── footer.html
│   │   └── member_socials.html
│   │
│   ├── Sobre/
│   │   └── sobrenos.html
│   │
│   ├── Integrantes/
│   │   └── nossotime.html
│   │
│   ├── Noticias/
│   │   ├── noticias.html
│   │   └── noticia_detalhe.html
│   │
│   ├── OBaDrones/
│   │   └── obadrones.html
│   │
│   ├── Colibri/
│   │   └── colibri.html
│   │
│   └── livro_de_visitas/
│       └── formulario.html
│
├── static/
│   ├── css/
│   │   ├── components/
│   │   │   ├── header.css
│   │   │   └── footer.css
│   │   ├── home.css
│   │   ├── sobrenos.css
│   │   ├── nossotime.css
│   │   ├── noticias.css
│   │   ├── noticia_detalhe.css
│   │   ├── obadrones.css
│   │   └── colibri.css
│   │
│   ├── js/
│   │   ├── formulario-cidades.js
│   │   ├── mapa-impacto.js
│   │   └── colibri-scroll.js
│   │
│   ├── img/
│   │   ├── colibri/
│   │   ├── footer/
│   │   ├── home/
│   │   ├── oba_drones/
│   │   └── sobre/
│   │
│   └── favicon.ico
│
├── media/
│   ├── integrantes/
│   └── noticias/
│
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Como executar

### Pré-requisitos

- Python instalado.
- Git instalado.
- Ambiente virtual Python.
- Dependências definidas em `requirements.txt`.

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd EducaDronesWeb
```

### 2. Criar o ambiente virtual

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

O projeto disponibiliza um arquivo `.env.example` como referência para configuração das variáveis necessárias.

Crie seu arquivo `.env` a partir dele e preencha os valores correspondentes.

**Atenção:** não compartilhe informações sensíveis, como chaves secretas e credenciais.

### 5. Executar as migrações

```bash
python manage.py migrate
```

### 6. Criar um superusuário

```bash
python manage.py createsuperuser
```

### 7. Iniciar o servidor

```bash
python manage.py runserver
```

A aplicação estará disponível em:

`http://127.0.0.1:8000/`

O painel administrativo poderá ser acessado em:

`http://127.0.0.1:8000/admin/`

## Testes

O projeto possui arquivos de testes nas aplicações `website`, `noticias`, `livro_de_visitas` e `emails`.

Para executar a suíte de testes do Django:

```bash
python manage.py test
```

Entre os testes identificados na aplicação `website`, estão:

- Verificação de carregamento das páginas institucionais.
- Verificação da seleção de notícias e conquistas em destaque.
- Verificação da listagem de notícias.
- Verificação do acesso aos detalhes de uma notícia por slug.
- Verificação do retorno 404 para notícias inexistentes.

## Publicação

Ainda não foi publicado.

## Desenvolvimento e manutenção

A organização modular permite que novas funcionalidades sejam adicionadas sem concentrar toda a lógica em uma única aplicação.

Para manutenção:

- Utilize os modelos Django para estruturar os dados.
- Utilize formulários para validação e processamento das entradas.
- Mantenha a lógica de apresentação nos templates.
- Organize os estilos por página ou componente.
- Utilize arquivos JavaScript separados para funcionalidades específicas.
- Crie migrações sempre que houver alterações nos modelos.
- Utilize o painel administrativo para gerenciar conteúdos que já possuem integração com o Django Admin.

---

## Equipe de Desenvolvimento

<div align="center">

  <table>
    <tr>
      <td align="center" width="200">
        <a href="https://github.com/geovane-nves">
          <img src="https://github.com/geovane-nves.png" width="100" height="100" style="border-radius: 50%;" alt="Foto de perfil de Desenvolvedor 1"/>
        </a>
        <br />
        <strong>Geovane Neves</strong>
        <br />
        <sub>Desenvolvedor, Organizador e UI/UX</sub>
        <br />
      </td>
      <td align="center" width="200">
        <a href="https://github.com/msantos7gabriel">
          <img src="https://github.com/msantos7gabriel.png" width="100" height="100" style="border-radius: 50%;" alt="Foto de perfil de Desenvolvedor 1"/>
        </a>
        <br />
        <strong>Gabriel Montalvão</strong>
        <br />
        <sub>Desenvolvedor</sub>
        <br />
      </td>
      <td align="center" width="200">
        <a href="https://github.com/R-Nhan">
          <img src="https://github.com/R-Nhan.png" width="100" height="100" style="border-radius: 50%;" alt="Foto de perfil de Desenvolvedor 1"/>
        </a>
        <br />
        <strong>Rubens Ian</strong>
        <br />
        <sub>Desenvolvedor</sub>
        <br />
      </td>
      <td align="center" width="200">
        <a href="https://github.com/Ray-Samuel">
          <img src="https://github.com/Ray-Samuel.png" width="100" height="100" style="border-radius: 50%;" alt="Foto de perfil de Desenvolvedor 1"/>
        </a>
        <br />
        <strong>Ray Samuel</strong>
        <br />
        <sub>Desenvolvedor</sub>
        <br />
      </td>
      <td align="center" width="200">
        <a href="https://github.com/OGustavoCosta">
          <img src="https://github.com/OGustavoCosta.png" width="100" height="100" style="border-radius: 50%;" alt="Foto de perfil de Desenvolvedor 1"/>
        </a>
        <br />
        <strong>Gustavo Costa</strong>
        <br />
        <sub>UI/UX</sub>
        <br />
      </td>
    </tr>
  </table>

</div>

---

<div align="center">
  <sub>Educa Drones · IF Baiano — Campus Guanambi</sub>
</div>
