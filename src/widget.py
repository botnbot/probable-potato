from datetime import datetime
from typing import Any

from src.masks import mask_card_number, mask_account


def mask_account_card(string: str) -> Any:
    """Функция, маскирующая счета и карты"""
    if "Счет " in string:
        account = string[-20:]
        return string[:-20] + mask_account(account)
    else:
        cardnumber = "".join(string[-16:].split())
        return string[:-16] + mask_card_number(cardnumber)


def get_data(date_str: str) -> str:
    """Функция, возвращающая строку с датой в формате DD.MM.YYYY"""
    no_format_date = datetime.strptime(date_str[:10], ("%Y-%m-%d"))
    format_date = no_format_date.strftime("%d.%m.%Y")
    return format_date

# print(mask_account_card('Maestro 1596837868705199'))