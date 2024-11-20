import requests
import dotenv
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

def shorten_link(telegram_token, long_url):
    url = 'https://api.vk.ru/method/utils.getShortLink'
    
    params = {
        "v": 5.199, 
        "url": long_url
    }
    headers = {
        "Authorization": f"Bearer {telegram_token}"
    }
    
    response = requests.post(url, headers=headers, params=params)
    response.raise_for_status()
    
    return response.json()["response"]["short_url"]


def count_clicks(telegram_token, short_link):
    url = 'https://api.vk.ru/method/utils.getLinkStats'
    
    params = {
        "v": 5.236,
        "interval": "forever",
        "key": short_link,
        "extended": 0
    }
    headers = {"Authorization": f"Bearer {telegram_token}"}
    
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    
    data = response.json()
    if "response" in data and "stats" in data["response"] and len(data["response"]["stats"]) > 0:
        return data["response"]["stats"][0]['views']
    else:
        return 0 # Или другое значение по умолчанию

def main():
    telegram_token = os.environ['TELEGRAM_TOKEN']
    parser = argparse.ArgumentParser( 
    description='Сокращение ссылок'
)
    parser.add_argument('user_url', help='Введите ссылку: ')
    args = parser.parse_args()
    # user_url = input("Введите ссылку: ")
    parsed_url = urlparse(args.user_url)
    
    try:
        if parsed_url.netloc == "vk.cc":
            try:
                clicks = count_clicks(telegram_token, parsed_url.path[1:])
                print("Количество кликов по ссылке:", clicks)
            except requests.exceptions.HTTPError as e:
                print(f"HTTP error при подсчете кликов: {e}")
        else:
            print("Сокращёная ссылка:", shorten_link(telegram_token, args.user_url))
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")


if __name__ == "__main__":
    main()