from typing import Generator


def cardnumber_generator(start: int, end: int) -> Generator:
    """Генератор номеров банковских карт"""
    for number in range(start, end + 1):
        cardnumber_str = f"{number:016d}"
        formatted_card_number = " ".join(cardnumber_str[i : i + 4] for i in range(0, 16, 4))
        yield formatted_card_number


def transaction_descriptions(transactions: list) -> Generator:
    """Функция которая выдает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def filter_by_currency_once(transactions: list, currency: str) -> Generator:
    """Функция которая выдает по очереди операции, в которых указана заданная валюта."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
