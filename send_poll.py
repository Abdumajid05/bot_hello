import requests
import os
from pprint import pprint
TOKEN = os.environ['TOKEN'] 

def send_poll(chat_id: int, question: str, options: list):
    """
    Send poll

    Args:
        chat_id (int): chat id
        question (str): question
        options (list): options
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    response = requests.post(URL, json={
        'chat_id': chat_id, 
        'question': question, 
        'options': options})
    return response.json()

chat_id = 86775091
question = 'What is your favorite programming language?'
options = [
    {'text': 'Python'},
    {'text': 'JavaScript'},
    {'text': 'C#'},
    {'text': 'Java'},
]
from pprint import pprint
pprint(send_poll(chat_id, question, options))