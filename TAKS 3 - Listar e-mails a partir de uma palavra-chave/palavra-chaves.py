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
        print("ocorreu um erro: " + error) 

def viewMessage(service, userID, msgID):
    try:
        message = service.users().messages().get(userId=userID, id=msgID, format='raw').execute() #returna a mensagem em formato raw codificado em base64
        msgStr = base64.urlsafe_b64decode(message['raw'].encode('ascii'))
        mime_msg = email.message_from_bytes(msgStr)
               
        contentType = mime_msg.get_content_maintype()
        if contentType == 'multipart':
            for part in mime_msg.get_payload():
                if part.get_content_maintype() == 'text/plain':
                    print(part.get_payload())
        elif contentType == 'text':
            print(mime_msg.get_payload())
        
    except Exception as error:
        print("ocorreu um erro: %s", error) 
        
    
def auth():
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


service = auth()
userID = 'me'    
q = "reembolso" 

IDs = searchStringMessage(service, userID, q)

for Ids in IDs:
    print(viewMessage(service, userID, Ids))