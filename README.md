# ToDo

Este repositório contém uma aplicação To-Do simples desenvolvida em Django. A aplicação permite aos usuários criar, visualizar, editar e excluir tarefas em uma lista de afazeres. Além disso, também inclui a funcionalidade de criar contas de usuários para autenticação.

## Funcionalidades

A aplicação To-Do inclui as seguintes funcionalidades:

- Criar uma nova conta de usuário
- Fazer login e logout
- Criar uma nova tarefa com título e descrição
- Visualizar todas as tarefas na lista de afazeres
- Marcar uma tarefa como concluída
- Editar o título e a descrição de uma tarefa existente
- Excluir uma tarefa da lista

## Requisitos

Para executar a aplicação em sua máquina local, você precisará ter os seguintes requisitos:

- Python 3.6 ou superior
- Django 3.0 ou superior

## Instalação

Siga as etapas abaixo para configurar e executar a aplicação:

1. Clone este repositório para o seu ambiente local usando o seguinte comando:

   ```
   git clone https://github.com/eduardoranucci/ToDo.git
   ```

2. Navegue até o diretório raiz do projeto:

   ```
   cd ToDo
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

5. Execute as migrações do banco de dados:

   ```
   python manage.py migrate
   ```

6. Inicie o servidor de desenvolvimento:

   ```
   python manage.py runserver
   ```

7. Acesse a aplicação em seu navegador em [http://localhost:8000/](http://localhost:8000/).

## Uso

Ao acessar a aplicação no navegador, você verá a página de login. Se você ainda não possui uma conta, clique em "Registrar" para criar uma nova conta de usuário. Após o registro, faça login com suas credenciais.

Uma vez autenticado, você poderá:

- Criar uma nova tarefa clicando no botão "Nova Tarefa" e preenchendo os campos do formulário.
- Visualizar todas as tarefas na lista de afazeres.
- Marcar uma tarefa como concluída, clicando na caixa de seleção ao lado da tarefa.
- Editar o título e a descrição de uma tarefa existente clicando no botão de edição.
- Excluir uma tarefa da lista clicando no botão de exclusão.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
