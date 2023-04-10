# Python Gmail API Quickstart: https://developers.google.com/gmail/api/quickstart/python
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# LEMBRE-SE: execute no terminal
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# antes de executar o script

# Se você modificar o SCOPES, delete o arquivo "token.json" caso esteja presente na pasta.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Básico do uso da API do Gmail:
    Lista as labels presentes no Gmail do usuário.
    """
    creds = None
    # O arquivo token.json armazena o acesso do usuário e tokens de refresh,
    # ele é criado AUTOMATICAMENTE quando o fluxo de autorização (authorization flow) é completado pela primeira vez
    # (você verá isso ocorrendo ao executar este script de maneira funcional pela primeira vez, abrirá uma guia no seu navegador com a mensagem sobre o "Authorization flow",
    # tal guia que você pode fechar assim que ela abre).
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Se não há credentials válido disponível no projeto, permite o usuário logar
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            
        # Salva as credenciais em um token para um próximo momento que for necessário.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Chama a API do Gmail.
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(label['name'])

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API. 
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()