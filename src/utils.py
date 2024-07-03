import json
from pathlib import Path
from typing import Any


def json_to_list(path_to_file: str) -> Any:
    """Функция преобразования JSON файла"""
    file_path = Path.cwd() / path_to_file
    try:
        with open(file_path, encoding="utf-8") as f:
            transactions = json.load(f)
        if not transactions:
            print(f"Файл '{file_path}' пустой.")
            return []
        return transactions

        if not isinstance(transactions, list):
            raise ValueError("Файл содержит не список")
            return []

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return []


# print(json_to_list("data\\operations22.json"))
