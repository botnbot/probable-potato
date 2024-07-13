import json
import logging
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

# Настройка логирования
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def file_to_list(path_to_file: str) -> List[Dict[str, Any]]:
    """Функция преобразования файлов с данными о транзакциях в список словарей.

    Поддерживаемые форматы: JSON, XLSX, CSV.
    """
    file_path = Path(path_to_file)
    transactions = []

    try:
        if not file_path.is_file():
            logger.error(f"Файл '{file_path}' не найден.")
            raise FileNotFoundError(f"Файл '{file_path}' не найден.")

        file_extension = file_path.suffix.lower()

        if file_extension == ".json":
            logger.info("Чтение JSON-файла")
            with open(file_path, encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                logger.error(f"JSON-файл '{file_path}' содержит не список")
                raise ValueError(f"JSON-файл '{file_path}' содержит не список")
            for item in data:
                if not isinstance(item, dict):
                    logger.error(f"JSON-файл '{file_path}' содержит элементы, которые не являются словарями")
                    raise ValueError(f"JSON-файл '{file_path}' содержит элементы, которые не являются словарями")
            transactions = data

        elif file_extension == ".xlsx":
            logger.info("Чтение XLSX-файла")
            excel_df = pd.read_excel(file_path)
            # Добавление нового столбца operationAmount
            excel_df["operationAmount"] = excel_df.apply(
                lambda row: {
                    "amount": row["amount"],
                    "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                },
                axis=1,
            )

            # Указание нового порядка столбцов
            new_col_order = ["id", "state", "date", "operationAmount", "description", "from", "to"]

            # Применение нового порядка столбцов
            excel_df = excel_df[new_col_order]

            # Преобразование DataFrame в список словарей
            transactions = excel_df.to_dict(orient="records")

        elif file_extension == ".csv":
            logger.info("Чтение CSV-файла")
            csv_df = pd.read_csv(file_path, delimiter=";")

            # Добавление нового столбца operationAmount
            csv_df["operationAmount"] = csv_df.apply(
                lambda row: {
                    "amount": row["amount"],
                    "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                },
                axis=1,
            )

            # Указание нового порядка столбцов
            new_col_order = ["id", "state", "date", "operationAmount", "description", "from", "to"]

            # Применение нового порядка столбцов
            csv_df = csv_df[new_col_order]

            # Преобразование DataFrame в список словарей
            transactions = csv_df.to_dict(orient="records")

        else:
            logger.error("Неподдерживаемый тип файла")
            raise ValueError("Неподдерживаемый тип файла")

    except FileNotFoundError:
        logger.error(f"Файл '{file_path}' не найден.")
        print(f"Файл '{file_path}' не найден.")
    except ValueError as e:
        logger.error(f"Произошла ошибка при чтении файла '{file_path}': {str(e)}")
        print(str(e))
    except Exception as e:
        logger.error(f"Произошла ошибка при чтении файла '{file_path}': {str(e)}")
        print(f"Произошла ошибка при чтении файла '{file_path}': {str(e)}")

    logger.info("Вывод результата")
    return transactions
