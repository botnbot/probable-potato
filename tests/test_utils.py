import json
from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.utils import file_to_list


@pytest.fixture
def setup_test_file(tmp_path):
    """Фикстура с данными транзакций"""
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
    """Проверка корректного JSON файла"""
    transactions = file_to_list(str(setup_test_file))
    assert len(transactions) == 3
    assert transactions[0]["currency"] == "USD"


def test_empty_json_file(tmp_path):
    """Проверка пустого JSON файла"""
    empty_file = tmp_path / "empty.json"
    with open(empty_file, "w", encoding="utf-8") as f:
        f.write("")
    transactions = file_to_list(str(empty_file))
    assert transactions == []


def test_non_list_json_file_invalid_data(tmp_path):
    """Проверка JSON файла с некорректными данными (не список)"""
    invalid_data = '{"id": 1, "amount": 100, "currency": "USD"}'
    invalid_file = tmp_path / "invalid_data.json"
    with open(invalid_file, "w", encoding="utf-8") as f:
        f.write(invalid_data)
    transactions = file_to_list(str(invalid_file))
    assert transactions == []


def test_non_list_json_file_invalid_format(tmp_path):
    """Проверка JSON файла с некорректным форматом (не JSON)"""
    invalid_data = "47"
    invalid_file = tmp_path / "invalid_format.json"
    with open(invalid_file, "w", encoding="utf-8") as f:
        f.write(invalid_data)
    transactions = file_to_list(str(invalid_file))
    assert transactions == []


def test_missing_json_file():
    """Проверка отсутствующего JSON файла"""
    missing_file = "nonexistent.json"
    transactions = file_to_list(missing_file)
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100, "currency": "USD"}]')
@patch("pathlib.Path.is_file", return_value=True)
def test_json_file(mock_is_file, mock_file):
    """Проверка чтения JSON файла с mock"""
    transactions = file_to_list("dummy_path.json")
    assert len(transactions) == 1
    assert transactions[0]["currency"] == "USD"


@patch("pandas.read_excel")
@patch("pathlib.Path.is_file", return_value=True)
def test_xlsx_file(mock_is_file, mock_read_excel):
    """Проверка чтения XLSX файла с mock"""
    mock_df = pd.DataFrame(
        {
            "id": [1, 2],
            "amount": [100, 200],
            "currency_name": ["USD", "EUR"],
            "currency_code": ["USD", "EUR"],
            "state": ["completed", "completed"],
            "date": ["2023-01-01", "2023-01-02"],
            "description": ["desc1", "desc2"],
            "from": ["account1", "account2"],
            "to": ["account3", "account4"],
        }
    )
    mock_read_excel.return_value = mock_df

    transactions = file_to_list("dummy_path.xlsx")
    assert len(transactions) == 2
    assert transactions[0]["operationAmount"]["currency"]["name"] == "USD"
    mock_read_excel.assert_called()


@patch("pandas.read_csv")
@patch("pathlib.Path.is_file", return_value=True)
def test_csv_file(mock_is_file, mock_read_csv):
    """Проверка чтения CSV файла с mock"""
    mock_df = pd.DataFrame(
        {
            "id": [1],
            "amount": [100],
            "currency_name": ["USD"],
            "currency_code": ["USD"],
            "state": ["completed"],
            "date": ["2023-01-01"],
            "description": ["desc1"],
            "from": ["account1"],
            "to": ["account3"],
        }
    )
    mock_read_csv.return_value = mock_df

    transactions = file_to_list("dummy_path.csv")
    assert len(transactions) == 1
    assert transactions[0]["operationAmount"]["currency"]["name"] == "USD"
    mock_read_csv.assert_called()
