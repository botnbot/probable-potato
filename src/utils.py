import json
import logging
from pathlib import Path
from typing import Any, Dict, List

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_formater = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)

def json_to_list(path_to_file: str) -> List[Dict[str, Any]]:
    """Функция преобразования JSON файла в список словарей с данными о транзакциях."""
    file_path = Path(path_to_file)
    transactions = []

    try:
        if not file_path.is_file():
            logger.error(f"Файл '{file_path}' не найден.")
            raise FileNotFoundError(f"Файл '{file_path}' не найден.")

        logger.info('Чтение JSON-файла')
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            logger.error(f"Файл '{file_path}' содержит не список")
            raise ValueError(f"Файл '{file_path}' содержит не список")
            transactions = []
        for item in data:

            if not isinstance(item, dict):
                logger.error(f"Файл '{file_path}' содержит элементы, которые не являются словарями")
                raise ValueError(f"Файл '{file_path}' содержит элементы, которые не являются словарями")

        transactions = data

    except FileNotFoundError:
        logger.error(f"Файл '{file_path}' не найден.")
        print(f"Файл '{file_path}' не найден.")
    except ValueError as e:
        logger.error(f"Произошла ошибка при чтении файла '{file_path}': {str(e)}")
        print(str(e))
    except Exception as e:
        logger.error(f"Произошла ошибка при чтении файла '{file_path}': {str(e)}")
        print(f"Произошла ошибка при чтении файла '{file_path}': {str(e)}")
    logger.info('Вывод  результата')
    return transactions


print(json_to_list("data\\operations22.json"))

