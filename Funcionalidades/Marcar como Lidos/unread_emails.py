# O script a seguir executa os seguintes passos:
# -Entra na inbox do gmail
# -Pega todas os emails não lidos
# -Extrai detalhes desses emails
# -Armazena os detalhes num aqruivo csv.
# -Marca aos emails como "Lidos"


# Importing required libraries
from apiclient import discovery
from apiclient import errors
from httplib2 import Http
from oauth2client import file, client, tools
import base64
from bs4 import BeautifulSoup
import re
import time
import dateutil.parser as parser
from datetime import datetime
import datetime
import csv

 
# Considero que você criou um projeto no console cloud google (link)
# E que lá no console cloud google, foi em 
# (menu de navegação > API e serviços > Tela de permissão OAuth > Usuários de teste) 
# e adicionou a sua conta (ou mais que uma) que vai utilizar como tester (usuário)
# Considero que você executou o primeiro arquivo para fazer a primeira conexão com a api do Gmail
# E que entre as labels presentes no seu gmail (que você pode verificar no output do primeiro arquivo), há as labels "INBOX" e "UNREAD"
# E que finalmente você tenha vindo pra esse arquivo

# No terminal, caso você não tenha já instalado na sua máquina, execute
# pip install oauth2client
# pip install beautifulsoup4
# pip install python-dateutile


# Creating a storage.JSON file with authentication details
# Cria um arquivo chamado "storage.json" com detalhes de autenticação (https://developers.google.com/workspace/guides/auth-overview?hl=pt-br#:~:text=O%20ato%20de%20garantir%20que%20um%20principal%2C%20que%20pode%20ser%20um%20usu%C3%A1rio%20ou%20um%20app%20agindo%20em%20nome%20de%20um%20usu%C3%A1rio%2C%20seja%20quem%20ele%20diz%20ser.%20Ao%20criar%20apps%20do%20Google%20Workspace%2C%20voc%C3%AA%20precisa%20conhecer%20estes%20tipos%20de%20autentica%C3%A7%C3%A3o%3A)
SCOPES = 'https://www.googleapis.com/auth/gmail.modify' # Embora o primeiro arquivo trabalhou com o escopo de readonly, agora usaremos o escopo de modify (que engloba o read) já que com ele podemos marcar quais emails foram lidos pelo programa
store = file.Storage('storage.json') 
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

user_id =  'me'
label_id_one = 'INBOX'
label_id_two = 'UNREAD'

# Getting all the unread messages from Inbox
# labelIds can be changed accordingly
# Solicita que o Gmail liste os emails da caixa de entrada do userId="me",
# mas APENAS os emails que estão listados na label "INBOX" e na label "UNREAD" ao mesmo tempo
# O maxResults=2 é serve para especificar que queremos apenas pegar os dois emails mais recentes das labels especificadas.
unread_msgs = GMAIL.users().messages().list(userId='me',labelIds=[label_id_one, label_id_two], maxResults=2).execute()

# Agore temos um dicionário.
# Portanto, a seguir as informações presentes em 'messages' são instanciadas.
mssg_list = unread_msgs['messages']

print ("Total unread messages in inbox: ", str(len(mssg_list)))

final_list = [ ]


for mssg in mssg_list:
	temp_dict = { }
	m_id = mssg['id'] # pega id de um email (mssg)
	message = GMAIL.users().messages().get(userId=user_id, id=m_id).execute() # usa a API pra pegar o conteúdo do email
	payld = message['payload'] # pega o payload (conteúdo bruto do email, que incluindo corpo, anexos, cabeçalho, entre outros metadados)
	headr = payld['headers'] # pega o cabeçalho presente no payload


	for one in headr: # pega o assunto do email (presente no cabeçalho)
		if one['name'] == 'Subject':
			msg_subject = one['value']
			temp_dict['Subject'] = msg_subject
		else:
			pass


	for two in headr: # pega a data (também presente no cabeçalho)
		if two['name'] == 'Date':
			msg_date = two['value']
			date_parse = (parser.parse(msg_date))
			m_date = (date_parse.date())
			temp_dict['Date'] = str(m_date)
		else:
			pass

	for three in headr: # pega o remetente (presente no cabeçalho)
		if three['name'] == 'From':
			msg_from = three['value']
			temp_dict['Sender'] = msg_from
		else:
			pass

	temp_dict['Snippet'] = message['snippet'] # pega o preview da mensagem do email


	try:
		
		# Pegando o corpo da mensagem
		mssg_parts = payld['parts'] # pega as partes do email (diferentes componentes que formam o conteúdo da email, e.g. texto puro e html)
		part_one  = mssg_parts[0] # pega primeiro elemento das partes do email
		part_body = part_one['body'] # pega corpo do email
		part_data = part_body['data'] # pega dados sorbe o corpo
		#"clean"s decoding de Base64 p/ UTF-8
		clean_one = part_data.replace("-","+")
		clean_one = clean_one.replace("_","/") 
		clean_two = base64.b64decode (bytes(clean_one, 'UTF-8')) 
		soup = BeautifulSoup(clean_two , "lxml" )
		mssg_body = soup.body() # mssg_body agora é uma forma legível de corpo de mensagem
		temp_dict['Message_body'] = mssg_body

	except :
		pass

	print(temp_dict)
	final_list.append(temp_dict) # acopla na lista final os dados de um email como um item de dicionário
	
	# Com a API, marcamos os emails como "Lidos" 
	GMAIL.users().messages().modify(userId=user_id, id=m_id,body={ 'removeLabelIds': ['UNREAD']}).execute() 
	



print ("Total messaged retrived: ", str(len(final_list)))

# A lista final é um dicionário no formato:
#   'Remetente': "'email.com' <name@email.com>",
#   'Assunto': "Lorem ipsum dolor it amet",
#   'Date': "yyyy-mm-dd",
#   'Preview': 'Lorem ipsum'
#   'Message_body': 'Lorem ipsum'

# Dicionário é armazendo como um csv.
with open('CSV_NAME.csv', 'w', encoding='utf-8', newline = '') as csvfile: 
    fieldnames = ['Sender','Subject','Date','Snippet','Message_body']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ',')
    writer.writeheader()
    for val in final_list:
    	writer.writerow(val)