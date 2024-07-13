from typing import List, Any, Dict


def search_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> dict:
    """Функция, возвращающая словарь с количеством операций по категориям"""
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction["description"]
        for category in categories:
            if category in description:
                category_count[category] += 1
    return category_count
