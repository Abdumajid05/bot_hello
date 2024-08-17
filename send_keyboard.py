import requests
import os
TOKEN = os.environ['TOKEN'] 
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'




def send_message(chat_id: int, text: str,reply_keyboard: list):
    """
    Send message

    Args:
        chat_id (int): chat id
        text (str): text
    """
    response = requests.post(URL, json={
        'chat_id': chat_id, 
        'text': text,
        'reply_markup':reply_keyboard 
        })
    return response.json()

chat_id = 86775091
text = 'Keyboard test'
# Keyboard button
button = {   
        'text': 'Button 1'
        }

# Keyboard
keyboard = [[button]]
# Reply keyboard
reply_keyboard = {
    'keyboard': keyboard
}

print(send_message(chat_id, text,reply_keyboard))


