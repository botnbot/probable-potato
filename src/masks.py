import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_formater = logging.Formatter('%(asctime)s -%(name)s -%(levelname)s: %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def mask_card_number(cardnumber: str) -> str:
    """Функция, маскирующая номер карты"""
    try:
        logger.info('Маскировка номера карты')
        masked_cardnumber_list = []
        masked_cardnumber = cardnumber[:-10] + "******" + cardnumber[-4:]

        for i in range(0, len(masked_cardnumber), 4):
            masked_cardnumber_list.append(masked_cardnumber[i: i + 4])

        result = " ".join(masked_cardnumber_list)
        logger.info('Номер карты успешно замаскирован')
        return result

    except Exception as e:
        logger.error(f'Ошибка при маскировке номера карты: {e}')

def mask_account(account: str) -> str:
    """Функция, маскирующая номер счета"""
    try:
        logger.info('Маскировка номера счета')
        result = "**" + account[-4:]
        logger.info('Номер счета успешно замаскирован')
        return result
    except Exception as e:
        logger.error(f'Ошибка при маскировке номера счета: {e}')
