# Busca por palavra chave na API Gmail

Realizar busca de uma ou mais palavras presente em um email, e listar todos os emails com tais palavras

## Como utilizar

* Gere uma credentials.json no google cloud
* Mais informações em: https://developers.google.com/gmail/api/quickstart/python
* Coloque o arquivo no workspace

### 1° forma
* Rode o código pelo comando abaixo ou então via vscode (recomendado)

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

