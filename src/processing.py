from typing import List, Any, Dict, Iterable
import re

def filter_by_currency(transactions: list, currency: str) -> List[dict]:
    """Функция которая выдает список транзакций, в которых указана заданная валюта."""
    filtered_by_currency = []
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
             filtered_by_currency.append(transaction)

    return filtered_by_currency


def filter_by_state(list_of_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрации транзакций по статусу (state) операции"""
    filtered_by_state = []
    for operation in list_of_operations:
        if operation.get("state") == state:
            filtered_by_state.append(operation)

    return filtered_by_state

def search_string_in_transactions(transactions: List[Dict[str, Any]], string_to_find: str) -> List[Dict[str, Any]]:
    '''Функция фильтрации транзакций по строке в описании'''
    list_of_selected_transactions =[]
    for transaction in transactions:
        if re.search(string_to_find, transaction["description"],flags=re.IGNORECASE) :
            list_of_selected_transactions.append(transaction)

    return list_of_selected_transactions


def sort_by_date(list_of_operations: Iterable, ascending: bool = True) -> list[dict]:
    """Функция сортировки по дате"""
    sorted_operations = sorted(
        list_of_operations, key=lambda list_of_operations: list_of_operations.get("date"), reverse=ascending
    )
    return sorted_operations
