# IMPORTS
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText


# AUTENTICAÇÃO - ESCOPOS
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 
          'https://www.googleapis.com/auth/gmail.modify']

# TOKEN
token = {
    "access_token": "YOUR_ACCESS_TOKEN",
    "expires_in": 3599,
    "refresh_token": "YOUR_REFRESH_TOKEN",
    "scope": "https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/gmail.modify",
    "client_id":"YOUR_CLIENT_ID",
    "client_secret":"YOUR_CLIENT_SECRET",
}

# AUTENTICAÇÃO
creds = Credentials.from_authorized_user_file('token.json', SCOPES)

service = build('gmail', 'v1', credentials=creds)

# CRIAR UMA CATEGORIA
label_body = {
    "name": "NOME_DA_CATEGORIA",
    "messageListVisibility": "show",
    "labelListVisibility": "labelShow",
}

categoria = service.users().labels().create(userId='me', body=label_body).execute()


# LISTAR EMAILS QUE TEM A PALAVRA QUE DESEJA FILTRAR NO ASSUNTO
mensagens = service.users().messages().list(userId='me', q='subject:(PALAVRA)', maxResults=10).execute()

# ROTULAR EMAILS NA CATEGORIA CRIADA
for mensagem in mensagens['messages']:
    label_body = {
        'removeLabelIds': ['IMPORTANT', 'CATEGORY_UPDATES', 'INBOX'],
        'addLabelIds': [categoria['id']]
    }
    service.users().messages().modify(userId='me', id=mensagem['id'], body=label_body).execute()