import requests
import os
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'




def send_message(chat_id: int, text: str):
    """
    Send message

    Args:
        chat_id (int): chat id
        text (str): text
    """
    response = requests.post(URL, params={'chat_id': chat_id, 'text': text, 'parse_mode': 'MarkdownV2'})
    return response.json()

chat_id = 86775091
text = '*Hello, World* from Python ||spoiler||'

print(send_message(chat_id, text))