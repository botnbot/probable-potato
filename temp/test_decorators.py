import pytest
from src.config import ROOT_PATH
from pathlib import Path
from src.decorators import log
@log(filename="log_file.txt")
def divide(a, b):
    '''Создаем тестовую функцию, которую будем использовать с декоратором'''
    return a / b


def test_successful_in_log():
    '''Проверяем, что лог записывается при успешном выполнении функции'''
    result = divide(4, 2)
    assert result == 2.0
    with open(Path(ROOT_PATH, "log_file.txt"), "r") as log_file:
        readable = log_file.read()
        assert "divide ok" in readable


def test_exception_in_log():
    '''Проверяем, что лог записывается при возникновении исключения в функции'''
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)
    with open(Path(ROOT_PATH, "../tests/log_file.txt"), "r") as log_file:
        readable = log_file.read()
        assert 'divide error' in readable
        assert 'ZeroDivisionError' in readable


@log()
def divide(x, y):
    return x / y


def test_successful_console(capsys):
    '''Проверяем вывод в консоль при успешном выполнении функции'''
    result = divide(6, 2)
    captured = capsys.readouterr()
    assert captured.out.strip().endswith("divide ok")


def test_exception_console(capsys):
    '''Проверяем вывод в консоль при возникновении исключения'''
    with pytest.raises(ZeroDivisionError):
        divide(8, 0)
    captured_err = capsys.readouterr()
    assert "divide error" in captured_err.out
    assert "ZeroDivisionError" in captured_err.out
