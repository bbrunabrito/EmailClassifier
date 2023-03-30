# Busca por palavra chave na API Gmail

Realizar busca de uma ou mais palavras presente em um email, e listar todos os emails com tais palavras

## Como utilizar

* Gere uma credentials.json no google cloud
* Mais informações em: https://developers.google.com/gmail/api/quickstart/python
* Coloque o arquivo no workspace
* instale o Google client library para python

### 1° forma

#### para instalar o Google client library
```python
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

* Rode o código pelo comando abaixo ou então execute via vscode (recomendado)

```bash
  python .\palavra-chaves.py
```
### 2° forma
* use o notebook e execute cédula por cédula

## Alterando palavra chave de busca
* No código, altere a variável "q" com o termo de pesquisa desejado
```python
# o nome do usuário e o termo a ser pesquisado.
userID = 'me'    
q = "problema" #altere aqui
```

## API Reference
recursos utilizados da API do Gmail

#### Uma mensagem de email

```
  users.messages
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | The immutable ID of the message. |
| `snippet`      | `string` | A short part of the message text. |
| `raw`      | `string` | The entire email message in an RFC 2822 formatted and base64url encoded string. Returned in messages.get and drafts.get responses when the format=RAW parameter is supplied. A base64-encoded string. |

https://developers.google.com/gmail/api/reference/rest/v1/users.messages

#### Receba uma mensagem específica

```
  users.messages.get
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `userId` | `string` | The user's email address. The special value me can be used to indicate the authenticated user.|
| `id` | `string` | The ID of the message to retrieve. This ID is usually retrieved using messages.list. The ID is also contained in the result when a message is inserted (messages.insert) or imported (messages.import). |

https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get

#### Lista as mensagens na caixa de email com base no termo de pesquisa

```
  users.messages.list
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `userId`      | `string` | The user's email address. The special value me can be used to indicate the authenticated user. |
| `q`      | `string` | Only return messages matching the specified query. Supports the same query format as the Gmail search box. Parameter cannot be used when accessing the api using the gmail.metadata scope. |

https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list

# Funções

### searchStringMessage(service, userID, searchString)
procura os emails com o termo específico e retorna uma lista com o ID dos emails


### viewMessageSnippet(service, userID, msgID)
Exibe o conteúdo do email, o assunto e o snippet.

### viewMessage(service, userID, msgID)
Exibe o conteúdo do email, em fullbody

### auth()
realiza a autenticação com a API e retorna um objeto service para futuras chamadas da API


