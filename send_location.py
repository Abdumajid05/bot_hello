import requests
import os
TOKEN = os.environ['TOKEN'] 

def send_location(chat_id: int, latitude: float, longitude: float):
    """
    Send location

    Args:
        chat_id (int): chat id
        latitude (float): latitude
        longitude (float): longitude
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/sendLocation'
    response = requests.get(URL, params={'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude})
    return response.json()


def send_venue(chat_id: int, latitude: float, longitude: float, title: str, address: str):
    """
    Send venue

    Args:
        chat_id (int): chat id
        latitude (float): latitude
        longitude (float): longitude
        title (str): title
        address (str): address
    """
    URL = f'https://api.telegram.org/bot{TOKEN}/sendVenue'
    response = requests.get(URL, params={'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude, 'title': title, 'address': address})
    return response.json()


chat_id = 86775091
latitude = 40.7128
longitude = -74.0060
title = 'CODESCHOOL'
address = 'Al-beruniy 84-uy'

# send_location(chat_id, latitude, longitude)
send_venue(chat_id, latitude, longitude, title, address)

