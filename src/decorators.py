from pathlib import Path

from src.config import ROOT_PATH


def log(filename=None):
    """Декоратор для логирования функции
    Аргумент функции - путь для сохранения лога функции
    Если аргумент не указан - лог выводится в консоль"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(Path(ROOT_PATH, filename), "a") as log_file:
                        log_file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(Path(ROOT_PATH, filename), "a") as log_file:
                        log_file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                raise e

        return wrapper

    return decorator
