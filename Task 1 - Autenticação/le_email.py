from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64

#Faz a verificação de credenciais
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
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
    
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

##############################################################

#Função que escreve os emails em um arquivo txt
def get_emails():
    with open('emails.txt', 'w', encoding='utf-8') as f:
        try:
            service = build('gmail', 'v1', credentials=creds)
            results = service.users().messages().list(userId='me', maxResults=10).execute()
            messages = results.get('messages', [])

            for message in messages:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                payload = msg['payload']
                headers = payload['headers']
                
                #Escreve o remetente, o assunto e a data
                for header in headers:
                    if header['name'] == 'From':
                        f.write(f"From: {header['value']}\n")
                    if header['name'] == 'Subject':
                        f.write(f"Subject: {header['value']}\n")
                    if header['name'] == 'Date':
                        f.write(f"Date: {header['value']}\n")
                
                #Se o corpo do email está vazio ou não segue o padrao MIME, a mensagem abaixo é escrita e o loop volta
                if 'parts' not in payload:
                    f.write("e-mail não contem nenhuma parte com o tipo MIME\n")
                    f.write("---------------------------------------------------------\n")    
                    continue
            
                #Escreve o corpo do email
                parts = payload['parts']
                for part in parts:
                    if part['mimeType'] == 'text/plain':
                        body = part['body']['data']
                        decoded_body = base64.urlsafe_b64decode(body).decode('utf-8')
                        f.write(f"Body: {decoded_body}\n")

                f.write("---------------------------------------------------------\n")
        except HttpError as error:
            f.write(f"An error occurred: {error}\n")
            messages = []

    return messages

get_emails()