# 📘 Atividade: Testing FastAPI Applications with pytest

## 🎯 Objetivo

Escreva testes automatizados para uma API FastAPI usando pytest e TestClient. Você verificará respostas HTTP, validação de dados e isolamento entre testes.

## 📝 Tarefas

### 🛠️ Preparar o ambiente e testar rotas básicas

#### Descrição

Copie `starter-code.py` para uma pasta de trabalho e renomeie-o para `app.py`. Na mesma pasta, crie `test_app.py`. Instale as dependências com `python -m pip install fastapi pytest httpx` e execute os testes com `pytest -q`.

#### Requisitos

A primeira parte da suíte de testes deve:

- Criar um cliente de teste com `fastapi.testclient.TestClient`, sem iniciar um servidor
- Verificar se `GET /health` retorna status `200` e `{"status": "ok"}`
- Verificar se `GET /books` retorna status `200` e uma lista JSON
- Isolar os testes limpando a lista em memória `books` antes de cada teste

### 🛠️ Testar cadastro e validação de livros

#### Descrição

Teste o cadastro de livros com dados válidos e inválidos. Use os endpoints e o modelo `Book` disponíveis em `app.py`.

#### Requisitos

A suíte de testes deve:

- Enviar um `POST /books` com `id`, `title` e `author` e verificar o status `201`
- Verificar se a resposta contém os dados enviados
- Confirmar que o livro cadastrado aparece em `GET /books`
- Enviar um livro sem um campo obrigatório e verificar o status `422`

### 🛠️ Testar consulta, exclusão e erros

#### Descrição

Complete a suíte verificando a busca e a exclusão por identificador, incluindo os casos em que o livro não existe.

#### Requisitos

A suíte de testes deve:

- Verificar se `GET /books/{book_id}` retorna status `200` e os dados do livro existente
- Verificar se a busca por um identificador inexistente retorna status `404`
- Verificar se `DELETE /books/{book_id}` retorna status `200` e remove o livro
- Confirmar que consultar o livro após a exclusão retorna status `404`
- Passar em execuções repetidas de `pytest -q`, sem depender da ordem dos testes
