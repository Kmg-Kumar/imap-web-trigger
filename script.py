#!/home/ubuntu/imap-web/env/bin python3
import requests
from imapclient import IMAPClient
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

imap_client = IMAPClient('imap.gmail.com', use_uid=False)

imap_client.login(os.environ.get('LISTENER_MAIL', ''), os.environ.get('LISTENER_MAIL_APP_PASSWORD', ''))
imap_client.select_folder('INBOX')
if os.environ.get('APP_ENV') == 'production':
    message = imap_client.search(['TO', 'demo@demo.com', 'UNSEEN'])
    app_url = os.environ.get('PRODUCTION_APP_URL')
else:
    message = imap_client.search(['FROM', 'staging@staging.com', 'UNSEEN'])
    app_url = os.environ.get('STAGING_APP_URL')

print(message)

if message:
    url = app_url
    response = requests.get(url)
    print(response)
else:
    print("No Mail Found")
