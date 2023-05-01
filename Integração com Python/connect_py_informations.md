# Parte 1 - Conexão Inicial

Para iniciar

https://developers.google.com/?hl=pt-br

canto superior esquerdo "products" e aperte "Google Workspace" 

ainda no canto superior esquerdo, vá em "Todos os produtos" e clique em "Gmail"

Aperte em "Guias" logo abaixo (ainda no canto superior esquerdo)

Pronto, estamos na visão geral da API do Gmail 

Requisitos:
1.  Ter vscode com python
2.  Ativar o serviço da API do Gmail (https://developers.google.com/gmail/api/quickstart/python?hl=pt-br no botão "Ativar a API")
3.  Pra que ativar seja possível, é necessário ter um projeto criado, ou melhor, tem que saber ao menos settar um projeto do google cloud platform 
4.  Portanto, caso não tenha um projeto e não saiba como criar um: siga passo a passo apenas até proceder com o penúltimo tópico "Add to your project folder and rename credentials.json" neste [link](https://chozinthet20602.medium.com/sending-email-with-python-using-gmail-api-33628e36306a#0bc0) (ou caso prefira aprender por vídeo, só proceda até o tópico "Enable api" do [link](https://chozinthet20602.medium.com/sending-email-with-python-using-gmail-api-33628e36306a#0bc0), e prossiga o passo a passo desse [vídeo](https://www.youtube.com/watch?v=7X3fBlMw_1k&ab_channel=JieJenn) até o tempo 4:39)
5.  Obs.: não é recomendável usar uma API key para esse caso, alguns serviços da api do gmail não deixam você ter acesso com uma tal API key que você tenha devido ao fato de alguns desses serviços exigirem o protocolo de autenticação 2.0 (OAuth2)
6.  Deve haver arquivo no tópico "OAuth 2.0 Client IDs", portanto, baixe o credential.json file do "Automation Script" no tópico "OAuth 2.0 client IDs" (arquivo que o autor do vídeo acima baixa e nomeia como "client.json" durante 4:39 e 5:12)
7.  Caso não haja nenhum arquivo no tópico "OAuth 2.0 Client IDs", clique em "+Create Credentials" no canto superior esquerdo, e faça o passo 6.
8.  Mude o nome do arquivo para "credentials.json", e coloque-o na pasta do projeto que você utilizará no VSCode.
9.  Baixe o arquivo "connect_python_w_api.py" e coloque-o na pasta do seu projeto.
10. Abra a pasta no VSCode
11. Opcionalmente você pode criar um ambiente virtual https://www.youtube.com/watch?v=m1TYpvIYm74&t=419s&ab_channel=Ot%C3%A1vioMiranda
----> ambiente virtual serve para garantir que um versionamento de um instalável que você vai utilizar pra esse projeto não seja o mesmo versionamento desse instalável para outro projeto, e isso ajuda em momentos que você está trabalhando com um projeto A que precisa de um instalável na versão X, enquanto você trabalha com outro projeto que precisa do mesmo instalável só que na versão Y. Criando um ambiente virtual para um projeto, você garante que não haja colisão entre os ambientes dos dois projetos.
12. Antes de executar o script de "connect_python_w_api_.py", escreva no terminal "pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib" para instalar os pacotes necessários para a conexão inicial.

O "connect_python_w_api.py" não é nada mais nada menos que o Quickstart.py que o Google fornece (Python Gmail API Quickstart: https://developers.google.com/gmail/api/quickstart/python)


## Descrição

O script em "connect_python_w_api.py" primeiramente importa os módulos necessários e define o escopo do acesso à API como somente leitura (readonly). Em seguida, ele verifica se o arquivo **token.json** existe no diretório atual. Se o arquivo existir, o código lê os tokens de acesso e de refresh do arquivo e cria um objeto **Credentials**. Se o arquivo não existir ou as credenciais não forem válidas, o código iniciará o fluxo de autenticação OAuth2 usando o file de client secrets (**credenciais.json**). Se as credenciais forem válidas, mas expiradas, o código atualizará o token de acesso usando o token de atualização.

Depois de obter as credenciais válidas, o código cria um objeto de serviço da API do Gmail e chama o método **users().labels().list()** pra buscar uma lista de labels presentes no gmail do usuário, e printa cada nome de label.



