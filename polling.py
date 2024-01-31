import requests
import time

from dotenv import find_dotenv, load_dotenv


env_file = find_dotenv('.env')
load_dotenv(env_file)

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = os.getenv('BOT_TOKEN')

offset = -2
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        print(updates['result'])
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
