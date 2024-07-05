import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv(".env")

apikey = os.getenv("API_KEY")
# transaction = {
#     "id": 550607912,
#     "state": "EXECUTED",
#     "date": "2018-07-31T12:25:32.579413",
#     "operationAmount": {"amount": "10", "currency": {"name": "USD", "code": "USD"}},
#     "description": "Перевод организации",
#     "from": "MasterCard 8532498887072395",
#     "to": "Счет 44238164562083919420",
# }


def convert_to_rub(transaction: dict) -> Any:
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": apikey}
    response = requests.request("GET", url, headers=headers)

    return response.json()["result"]
