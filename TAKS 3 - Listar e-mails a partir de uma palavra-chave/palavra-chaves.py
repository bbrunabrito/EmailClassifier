from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
import email

# If modifying these scopes, delete the file token.pickle.
#Escopo de permissão da API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def searchStringMessage(service, userID, searchString):
    """
    Esta função irá retornar a lista com ID das mensagem que possuem a string (palavra) em questão
    Args:
        service: autenticação da API
        userID: id do usuário, no caso, o cliente, será sempre "me"(eu)
        searchString: apenas retornará as mensagem com o texto ou palavra presente presente
    Returns: lista com todos os IDs com a searchString em específico.
    """
    try: 
        idList = [] #inicializando a lista
        
        #adquirindo a mensagem (aonde a mágica acontece!)
        searchIds = service.users().messages().list(userId=userID, q=searchString).execute()
        
        try:
            EmailIds = searchIds ['messages']
        except KeyError:
            print("retornado 0 resultados")
            return idList
        
        if len(EmailIds)>=1:    #anexa todos os emails na lista "idList"
            for msg_id in EmailIds:
                idList.append(msg_id['id'])
            return (idList)
    except HttpError as error:
        print("ocorreu um erro: %s", error) 

def viewMessage(service, userID, msgID):
    """
    Esta função mostra os emails presente na lista de ID
    Args:
        service: autenticação da API
        userID: id do usuário, no caso, o cliente, será sempre "me"(eu)
        msgID: iD da mensagem em questão
    Returns: o email em sua parte texto e html
    """
    try:
        message = service.users().messages().get(userId=userID, id=msgID, format='raw').execute() #retorna a mensagem em formato raw codificado em base64
        mime_msg = email.message_from_bytes(base64.urlsafe_b64decode(message['raw']))
        
        print("-----")        
        contentType = mime_msg.get_content_maintype()
        if contentType == 'multipart':
            for part in mime_msg.get_payload():
                if part.get_content_maintype() == 'text':
                    print(part.get_payload())
        elif contentType == 'text':
            print(mime_msg.get_payload())
        print("-----")
        
    except Exception as error:
        print("ocorreu um erro: %s", error)

def viewMessageSnippet(service, userID, msgID):
    """
    Esta função mostra os emails presente na lista de ID, apenas o subject e o snippet da mensagem
    Args:
        service: autenticação da API
        userID: id do usuário, no caso, o cliente, será sempre "me"(eu)
        msgID: iD da mensagem em questão
    Returns: o snippet do email
    """
    try:
        message = service.users().messages().get(userId=userID, id=msgID, format='raw').execute() #retorna a mensagem em formato raw codificado em base64
        mime_msg = email.message_from_bytes(base64.urlsafe_b64decode(message['raw']))
        
        #print(mime_msg['from']) mostrar o email do remetente       
        #print(mime_msg['to'])  mostrar o email do destinatário
        print(mime_msg['subject'])
        print(message['snippet'])
        print(' ')
        
    except Exception as error:
        print("ocorreu um erro: %s", error) 
        

#OBS: necessário arquivo credentials.json na workspace
#Caso queira refazer a conexão, basta apagar o arquivo token.json na workspace
def auth():
    """Conexão com a API para autenticação

    Returns: um objeto "service" para futuras chamadas de API.
    """
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            
    service = build('gmail', 'v1', credentials=creds)
    return service


#conexão com a API via auth e retornar um objeto (service) 
service = auth()
# o nome do usuário e o termo a ser pesquisado.
userID = 'me'    
q = "problema" 

#salvar a pesquisa em "IDs" e logo em seguida exibir
IDs = searchStringMessage(service, userID, q)
print(IDs)

#visualizar as mensagens de cada ID.
for i in IDs:
    print(viewMessageSnippet(service, userID, i))

for i in IDs:
    print(viewMessage(service, userID, i))