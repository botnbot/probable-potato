from typing import Iterable


def filter_by_state(list_of_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрации по статусу (state) операции"""
    list_of_selected_operations = []
    for operation in list_of_operations:
        if operation.get("state") == state:
            list_of_selected_operations.append(operation)

    return list_of_selected_operations

print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                              {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                              {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))


def sort_by_date(list_of_operations: Iterable, ascending: bool = True) -> list[dict]:
    """Функция сортировки по дате"""
    sorted_operations = sorted(
        list_of_operations, key=lambda list_of_operations: list_of_operations.get("date"), reverse=ascending
    )
    return sorted_operations
