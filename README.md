# CRUD-DB-fastAPI

Este projeto é uma API desenvolvida com **FastAPI**, **Pydantic** e **SQLAlchemy**, utilizando **PostgreSQL** como banco de dados. A API permite o cadastro de empresas e a gestão de obrigações acessórias que precisam ser declaradas ao governo.

---

## Tecnologias Utilizadas

- **FastAPI**: Framework moderno e rápido para a criação de APIs RESTful.
- **Pydantic**: Biblioteca para validação de dados e criação de modelos (usado para definir os modelos de dados).
- **SQLAlchemy**: ORM (Object-Relational Mapper) para interação com o banco de dados.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar os dados da API.

---

## Como Utilizar

### 1. Pré-requisitos

- **Python** 3.8 ou superior
- **Acesso** Confira se a porta 5432 está liberada na sua máquina, para o uso do postgreSQL

### 2. Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/EricM1303/CRUD-DB-fastAPI.git
   cd CRUD-DB-fastAPI
   ```
2. Baixe as dependências:
    ```bash	
    python -r requirements.txt
    ```
3. Crie o .ENV:
    ```bash
    mkdir .env
    ```
4. Edite o .ENV:
- É importante que edite corretamente o ENV:
    - insira URL_DATABASE='postgresql://usuario:senha@localhost:porta/nome-do-banco'

5. Execução:
    ```bash
    uvicorn main:app --reload
    ```
---
## Acessar URL da API
Para acessar sua aplicação, é necessário entrar na URL que o **FastAPI** gera ao inicia-lo com na etapa **5** e inserir o /docs ao final da URL.
- localhost:5000/docs **(exemplo)**

---
