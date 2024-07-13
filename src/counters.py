from typing import List, Any, Dict
from collections import Counter


def search_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> dict:
    """Функция, возвращающая словарь с количеством операций по категориям"""
    category_count = Counter()
    for transaction in transactions:
        if transaction["state"] in categories:
            category_count[transaction['state']] += 1
    return dict(category_count)
