from datetime import datetime


def get_data(date_str: str) -> str:
    """Функция, возвращающая строку с датой в формате DD.MM.YYYY """
    no_format_date = datetime.strptime(date_str[:10], ("%Y-%m-%d"))
    format_date= no_format_date.strftime("%d.%m.%Y")
    print(no_format_date)
    return format_date
print(get_data('2018-07-31T02:26:18.671407'))