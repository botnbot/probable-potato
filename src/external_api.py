import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv(".env")

apikey = os.getenv("API_KEY")

def convert_to_rub(transaction: dict) -> Any:
    '''Функция конвертация валюты транзакции в рубли'''
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": apikey}
    response = requests.request("GET", url, headers=headers)

    return response.json()["result"]
