from src.utils import file_to_list
from src.processing import filter_by_state, sort_by_date, filter_by_currency, search_string_in_transactions
from src.widget import get_data, mask_account_card
import pandas as pd

print(
    """Привет!
Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
)

menu = ""
while menu not in (1, 2, 3):
    menu = int(input("Введите номер "))
    if menu not in (1, 2, 3):
        print("Некорректный ввод. Повторите \n")
if menu == 1:
    transactions = file_to_list("data/operations22.json")
    print("Для обработки выбран JSON-файл")
elif menu == 2:
    transactions = file_to_list("data/transactions.csv")
    print("Для обработки выбран csv-файл")
elif menu == 3:
    transactions = file_to_list("data/transactions_excel.xlsx")
    print("Для обработки выбран excel-файл")

status = ""
while status not in ("EXECUTED", "CANCELED", "PENDING"):
    status = input(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED CANCELED PENDING  \n"""
    )
    if status not in ("EXECUTED", "CANCELED", "PENDING"):
        print(f"Статус операции {status} недоступен.")
print(f"Операции фильтруются по статусу {status}")
filtered_by_state = filter_by_state(transactions, status)

is_sort_by_date = ""
while is_sort_by_date not in ("да", "нет"):
    is_sort_by_date = (input("Отсортировать операции по дате? Да/Нет \n")).lower()
    if is_sort_by_date not in ("да", "нет"):
        print("Ответ не распознан. Введите Да или Нет")

if is_sort_by_date == "да":
    print("Транзакции сортируются по дате")
    order = ""
    while order not in ("по возрастанию", "по убыванию"):
        order = (input("Отсортировать по возрастанию или по убыванию? \n")).lower()
        if order not in ("по возрастанию", "по убыванию"):
            print("Ответ не распознан. Наберите по возрастанию или по убыванию")
        if order == "по убыванию":
            print(order)
            ascending = True
            sorted_by_date = sort_by_date(filtered_by_state, ascending)
        else:
            order = "по возрастанию"
            print(order)
            ascending = False
            sorted_by_date = sort_by_date(filtered_by_state, ascending)
else:
    print("Транзакции не сортируются по дате")
    sorted_by_date = filtered_by_state


filter_by_rub = ""
while filter_by_rub not in ("да", "нет"):
    filter_by_rub = (input("Выводить только рублевые транзакции? Да/Нет \n")).lower()
    if filter_by_rub not in ("да", "нет"):
        print("Ответ не распознан. Наберите Да или Нет")
    print(filter_by_rub)
if filter_by_rub == "да":
    filtered_by_rub = filter_by_currency(sorted_by_date, "RUB")
else:
    filtered_by_rub = sorted_by_date


filter_by_string = ""
while filter_by_string not in ("да", "нет"):
    filter_by_string = (input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n")).lower()
    if filter_by_string not in ("да", "нет"):
        print("Ответ не распознан. Наберите Да или Нет")

if filter_by_string == "да":
    string_to_find = input("Введите строку для поиска ")
    filtered_by_string = search_string_in_transactions(filtered_by_rub, string_to_find)
else:
    filtered_by_string = filtered_by_rub

print("Распечатываю итоговый список транзакций...")
if filtered_by_string:
    print(f"Всего {len(filtered_by_string)} операций в выборке")

    for transaction in filtered_by_string:
        frm = (
            str(mask_account_card(transaction["from"])) + " -> "
            if "from" in transaction and pd.notna(transaction["from"])
            else ""
        )
        to = mask_account_card(transaction["to"]) if "to" in transaction and pd.notna(transaction["to"]) else ""
        date = get_data(str(transaction["date"])) if "date" in transaction and pd.notna(transaction["date"]) else ""
        description = (
            transaction["description"] if "description" in transaction and pd.notna(transaction["description"]) else ""
        )
        amount = (
            transaction["operationAmount"]["amount"]
            if "operationAmount" in transaction and pd.notna(transaction["operationAmount"]["amount"])
            else ""
        )
        name = (
            transaction["operationAmount"]["currency"]["name"]
            if "operationAmount" in transaction and pd.notna(transaction["operationAmount"]["currency"]["name"])
            else ""
        )

        print(date, description)
        print(frm, to)
        print(f"Сумма:  {amount} {name} \n")

else:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
