# Projeto RAG com Langchain

Este projeto é um exemplo de RAG (Retrieval-Augmented Generation) usando Langchain em Python. Ele utiliza os primeiros livros de Harry Potter em formato markdown para demonstrar como carregar documentos, dividi-los em chunks, salvar em uma base de dados Chroma e, finalmente, responder perguntas com base nesses documentos.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes programas instalados:

- Python 3.7+
- pip (gerenciador de pacotes do Python)
- Uma conta na OpenAI e a respectiva chave API

## Instalação

1. Clone o repositório e entre no diretório do projeto.

2. Crie um ambiente virtual e ative-o.

3. Instale as dependências listadas no arquivo `requirements.txt`.

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave API da OpenAI.

5. Coloque os arquivos markdown dos livros de Harry Potter na pasta `data/`.

## Uso

### Preparar a Base de Dados

Execute o script `create_database.py` para carregar os documentos, dividi-los em chunks e salvar em uma base de dados Chroma.

```bash
python create_database.py
```

### Fazer Perguntas

```bash
python query_data.py "Sua pergunta aqui"
```

Use o script `query_data.py` para fazer perguntas baseadas nos documentos carregados.

## Estrutura dos Arquivos

- `prepare_data.py`: Script para carregar documentos, dividir em chunks e salvar no Chroma.
- `query_data.py`: Script para fazer perguntas e obter respostas baseadas nos documentos.
- `data/`: Diretório onde os arquivos markdown dos livros devem ser colocados.
- `chroma/`: Diretório onde a base de dados Chroma será salva.
- `.env`: Arquivo para armazenar a chave API da OpenAI.

## Exemplo

Para fazer uma pergunta sobre os livros de Harry Potter, execute o script `query_data.py` com a sua pergunta.

```bash
python query_data.py "Qual é o nome do melhor amigo de Harry Potter?"
```

A resposta será baseada no contexto dos documentos carregados e salvos na base de dados.


