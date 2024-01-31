import os
import requests
import time

from dotenv import find_dotenv, load_dotenv

API_URL = 'https://api.telegram.org/bot'


env_file = find_dotenv('.env')
load_dotenv(env_file)
BOT_TOKEN = os.getenv('BOT_TOKEN')

offset = -2
timeout = 0
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True: 
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
    print(updates)

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
