import pytest
from src.generators import transaction_descriptions, filter_by_currency, cardnumber_generator


def test_cardnumber_generator():
    expected_output = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]
    assert list(cardnumber_generator(1, 5)) == expected_output

def test_empty_list():
    transactions = []
    gen = transaction_descriptions(transactions)
    with pytest.raises(StopIteration):
        next(gen)


def test_single_transaction():
    transactions = [{"description": "Перевод со счета на счет"}]
    gen = transaction_descriptions(transactions)
    assert next(gen) == "Перевод со счета на счет"
    with pytest.raises(StopIteration):
        next(gen)


def test_multiple_transactions():
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"}
    ]
    gen = transaction_descriptions(transactions)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"
    with pytest.raises(StopIteration):
        next(gen)


def test_missing_description_key():
    transactions = [{"amount": 100}]
    gen = transaction_descriptions(transactions)
    with pytest.raises(KeyError):
        next(gen)


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


def test_filter_by_currency_with_matching_currency(sample_transactions):
    filtered_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(filtered_transactions) == 3
    assert all(transaction["operationAmount"]["currency"]["code"] == "USD" for transaction in filtered_transactions)


def test_filter_by_currency_with_no_matching_currency(sample_transactions):
    filtered_transactions = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(filtered_transactions) == 0


def test_filter_by_currency_with_empty_transactions():
    filtered_transactions = list(filter_by_currency([], "USD"))
    assert len(filtered_transactions) == 0


