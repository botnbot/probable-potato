def mask_card_number(cardnumber: str) -> str:
    """Функция, маскирующая номер карты"""
    masked_cardnumber_list = []
    masked_cardnumber = cardnumber[:-10] + "******" + cardnumber[-4:]

    for i in range(0, len(masked_cardnumber), 4):
        masked_cardnumber_list.append(masked_cardnumber[i: i + 4])

    return " ".join(masked_cardnumber_list)


def mask_account(account: str) -> str:
    """Функция, маскирующая номер счета"""
    return "**" + account[-4:]
