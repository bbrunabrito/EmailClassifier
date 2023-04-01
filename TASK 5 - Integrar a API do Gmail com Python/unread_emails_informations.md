# Parte 2 - Lendo emails Unread

O script de "unread_emails" executa os seguintes passos:
  -Entra na inbox do gmail
  -Pega todas os emails não lidos
  -Extrai detalhes desses emails (remetente, assunto, data, preview e corpo da mensagem.)
  -Armazena os detalhes num arquivo csv.
  -Marca os emails como "Lidos"

Observação:
1. Esse arquivo deve ser colocado junto com a pasta do seu projeto após ter executado o "connect_python_w_api.py"
2. Para esse programa, estou considerando que você já criou um projeto no console cloud google
3. E que lá no console cloud google, foi em 
(menu de navegação > API e serviços > Tela de permissão OAuth > Usuários de teste) 
e adicionou a sua conta (ou mais que uma) que vai utilizar o script como tester (usuário)
4. Considero que você executou o primeiro arquivo para fazer a primeira conexão com a api do Gmail
5. Considero que já existe um arquivo "credentials.json" em meio a pasta e um arquivo "token.json"
5. E que entre as labels presentes no seu gmail (que você pode verificar no output do primeiro arquivo), há as labels "INBOX" e "UNREAD"
6. Para que finalmente você possa usar plenamente este arquivo e seguir as instruções



Instruçòes:
 No terminal, caso você não tenha já instalado na sua máquina, execute:
 pip install oauth2client
 pip install beautifulsoup4
 pip install python-dateutile

