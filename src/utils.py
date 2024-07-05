import json
from pathlib import Path
from typing import Any, List, Dict


def json_to_list(path_to_file: str) -> List[Dict[str, Any]]:
    """Функция преобразования JSON файла в список словарей с данными о транзакциях."""
    file_path = Path(path_to_file)
    transactions = []

    try:
        if not file_path.is_file():
            raise FileNotFoundError(f"Файл '{file_path}' не найден.")

        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError(f"Файл '{file_path}' содержит не список")

        for item in data:
            if not isinstance(item, dict):
                raise ValueError(f"Файл '{file_path}' содержит элементы, которые не являются словарями")

        transactions = data

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{file_path}': {str(e)}")

    return transactions


print(json_to_list("data\\operations22.json"))
