import pytest
from src.decorators import log
from src.config import ROOT_PATH
from pathlib import Path


@log(filename=Path(ROOT_PATH, "../src/log_file.txt"))
def divide(a, b):
    """Тестовая функция, которую будем использовать в тестах декоратора"""
    return a / b


def test_log_successful():
    """Проверяем, что лог записывается при успешном выполнении функции"""
    log_file = Path(ROOT_PATH, "../src/log_file.txt")
    result = divide(4, 2)
    assert result == 2.0
    with open(log_file, "r") as f:
        readable = f.read()
        assert "divide ok" in readable


def test_log_err():
    """Проверяем, что лог записывается при возникновении исключения"""
    log_file = Path(ROOT_PATH, "../src/log_file.txt")
    with pytest.raises(TypeError):
        divide(1, "2")
    assert log_file.exists()
    with open(log_file, "r") as f:
        log_contents = f.read()
        assert "divide error: unsupported operand type(s) for /: 'int' and 'str'. Inputs: (1, '2'), {}" in log_contents
