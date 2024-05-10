# Securitas Cursos

Securitas Cursos é uma plataforma de cursos voltada para segurança do trabalho.

## Acesso ao Programa

Siga os passos abaixo para clonar o projeto, criar e ativar um ambiente virtual e instalar as dependências:

### 1. Clonar o Projeto

Clone o repositório do GitHub para o seu ambiente local:

``` bash
https://github.com/johnhiguwww/securitas_cursos.git
```

### 2. Criar e Ativar o Ambiente Virtual
Navegue até o diretório do projeto e crie um ambiente virtual:
``` bash
cd securitas-cursos
python -m venv venv
```
Em seguida, ative o ambiente virtual:

- No Windows:
``` bash
venv\Scripts\activate
```

- No macOS e Linux:
``` bash
source venv/bin/activate
```
### 3. Instalar Dependências
Com o ambiente virtual ativado, instale as dependências do projeto usando o arquivo requirements.txt:
``` bash
pip install -r requirements.txt
```
### 4. Configurar o Banco de Dados
Antes de rodar a aplicação, você precisa configurar o banco de dados. Abra o arquivo **securitas_cursos/settings.py** e ajuste as configurações do banco de dados conforme necessário.

### 5. Criar as Migrações e Aplicar no Banco de Dados
Execute os seguintes comandos para criar as migrações e aplicá-las ao banco de dados:
``` bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Criar um Superusuário
Para acessar o painel administrativo e gerenciar os cursos, crie um superusuário executando o seguinte comando e siga as instruções:
``` bash
python manage.py createsuperuser
```

    **USERNAME: "securitas_cursos_adm"**
    **PASSWORD: "SZ.bhU75Y?]gBv;"**

### 7. Rodar a Aplicação

Por fim, rode o servidor de desenvolvimento Django:
``` bash
python manage.py runserver
```
Agora você pode acessar a aplicação em[]( http://127.0.0.1:8000/).

### Informações para Cadastro de Usuários Comuns
Para cadastrar usuários comuns, utilize as seguintes credenciais nos campos apropriados:

    USERNAME: "securitas_cursos_adm"
    PASSWORD: "SZ.bhU75Y?]gBv;"
