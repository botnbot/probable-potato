from typing import Iterable


def filter_by_state(list_of_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрации по статусу (state) операции"""
    list_of_selected_operations = []
    for operation in list_of_operations:
        if operation.get("state") == state:
            list_of_selected_operations.append(operation)

    return list_of_selected_operations


def sort_by_date(list_of_operations: Iterable, ascending: bool = True) -> list[dict]:
    """Функция сортировки по дате"""
    sorted_operations = sorted(
        list_of_operations, key=lambda list_of_operations: list_of_operations.get("date"), reverse=ascending
    )
    return sorted_operations
