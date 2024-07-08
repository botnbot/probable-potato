import pytest
import json
from src.utils import json_to_list


@pytest.fixture
def setup_test_file(tmp_path):
    '''Фикстура с данными транзакций'''
    test_data = [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"},
        {"id": 3, "amount": 150, "currency": "GBP"},
    ]
    test_file = tmp_path / "operations22.json"
    with open(test_file, "w", encoding="utf-8") as f:
        json.dump(test_data, f)
    return test_file


def test_valid_json_file(setup_test_file):
    '''Проверка корректного JSON файла'''
    transactions = json_to_list(str(setup_test_file))
    assert len(transactions) == 3
    assert transactions[0]["currency"] == "USD"


def test_empty_json_file(tmp_path):
    '''Проверка пустого JSON файла'''
    empty_file = tmp_path / "empty.json"
    with open(empty_file, "w", encoding="utf-8") as f:
        f.write("")
    transactions = json_to_list(str(empty_file))
    assert transactions == []


def test_non_list_json_file_invalid_data(tmp_path):
    '''Проверка JSON файла с некорректными данными (не список)'''
    invalid_data = '{"id": 1, "amount": 100, "currency": "USD"}'
    invalid_file = tmp_path / "invalid_data.json"
    with open(invalid_file, "w", encoding="utf-8") as f:
        f.write(invalid_data)
    transactions = json_to_list(str(invalid_file))
    assert transactions == []


def test_non_list_json_file_invalid_format(tmp_path):
    '''Проверка JSON файла с некорректным форматом (не JSON)'''
    invalid_data = "47"
    invalid_file = tmp_path / "invalid_format.json"
    with open(invalid_file, "w", encoding="utf-8") as f:
        f.write(invalid_data)
    transactions = json_to_list(str(invalid_file))
    assert transactions == []


def test_missing_json_file():
    '''Проверка отсутствующего JSON файла'''
    missing_file = "nonexistent.json"
    transactions = json_to_list(missing_file)
    assert transactions == []
