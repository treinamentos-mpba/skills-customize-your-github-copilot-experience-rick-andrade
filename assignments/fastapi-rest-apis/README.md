# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST com FastAPI para cadastrar e consultar livros. Você praticará rotas HTTP, dados JSON, modelos de validação com Pydantic e respostas de erro.

## 📝 Tarefas

### 🛠️ Criar o aplicativo e uma rota de saúde

#### Descrição

Use o arquivo inicial para executar uma aplicação FastAPI e verificar se ela está disponível. Instale as dependências com `python -m pip install fastapi uvicorn` e inicie o servidor com `uvicorn starter-code:app --reload`.

#### Requisitos

O aplicativo deve:

- Criar uma instância FastAPI chamada `app`
- Disponibilizar `GET /health`
- Retornar `{"status": "ok"}` como resposta JSON
- Permitir que a documentação interativa seja acessada em `/docs`

### 🛠️ Cadastrar e listar livros

#### Descrição

Crie um modelo Pydantic para representar um livro e implemente operações para cadastrar livros e listar os livros cadastrados. Mantenha os dados em uma lista em memória; eles não precisam continuar salvos depois que o servidor for encerrado.

#### Requisitos

A API deve:

- Definir um modelo `Book` com os campos `id` (inteiro), `title` (texto) e `author` (texto)
- Disponibilizar `GET /books` para retornar todos os livros como JSON
- Disponibilizar `POST /books` para validar, cadastrar e retornar um livro
- Aceitar no corpo de `POST /books` um JSON como:

```json
{
  "id": 1,
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```

### 🛠️ Consultar e excluir um livro

#### Descrição

Adicione operações para localizar um livro pelo seu identificador e removê-lo da lista. Use a interface `/docs` para testar os diferentes caminhos, inclusive uma busca por um identificador inexistente.

#### Requisitos

A API deve:

- Disponibilizar `GET /books/{book_id}` para retornar o livro correspondente
- Disponibilizar `DELETE /books/{book_id}` para remover o livro correspondente
- Retornar o status HTTP `404` com uma mensagem clara quando o identificador não existir
- Confirmar a exclusão por meio da resposta de `DELETE`
