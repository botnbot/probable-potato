from unittest.mock import patch
import pytest
import os
import requests
from dotenv import load_dotenv
from typing import Any

load_dotenv(".env")

apikey = os.getenv("API_KEY")


@pytest.fixture
def transaction_fix():
    """Фикстура транзакции"""
    return {
        "id": 550607912,
        "state": "EXECUTED",
        "date": "2018-07-31T12:25:32.579413",
        "operationAmount": {"amount": 10, "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 8532498887072395",
        "to": "Счет 44238164562083919420",
    }


@patch("requests.request")
def test_convert_to_rub(mock_request, transaction_fix) -> Any:
    """Тест на соответствие ответа ожидаемому от API"""
    amount = transaction_fix["operationAmount"]["amount"]
    currency = transaction_fix["operationAmount"]["currency"]["code"]

    mock_response = {
        "success": True,
        "query": {"from": "USD", "to": "sort_for_rub", "amount": 10},
        "info": {"timestamp": 1720029425, "rate": 87.849598},
        "date": "2024-07-03",
        "result": 878.49598,
    }
    mock_request.return_value.json.return_value = mock_response

    # Вызов функции, которая использует requests.request
    result = convert_to_rub(transaction_fix)

    mock_request.assert_called_once_with(
        "GET",
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}",
        headers={"apikey": apikey},
    )

    assert result == mock_response


def convert_to_rub(transaction: dict) -> dict:
    """Тестируемая функция"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": apikey}
    response = requests.request("GET", url, headers=headers)

    return response.json()
