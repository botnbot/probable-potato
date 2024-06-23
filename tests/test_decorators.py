import pytest

from src.decorators_2 import log


@log(filename="test.log")
def divide(a, b):
    '''Создаем тестовую функцию, которую будем использовать с декоратором'''
    return a / b


def test_successful():
    '''Проверяем, что лог записывается при успешном выполнении функции'''
    result = divide(4, 2)
    assert result == 2.0
    with open("test.log", "r") as log_file:
        readable = log_file.read()
        assert "divide ok" in readable


def test_exception():
    '''Проверяем, что лог записывается при возникновении исключения в функции'''
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)
    with open("test.log", "r") as log_file:
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
    print(f"Captured output: {captured_err.out}")
    assert "divide error" in captured_err.out
    assert "ZeroDivisionError" in captured_err.out
