import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def mask_card_number(cardnumber: str) -> str:
    """Функция, маскирующая номер карты"""
    try:
        masked_cardnumber_list = []
        masked_cardnumber = cardnumber[:-10] + "******" + cardnumber[-4:]
        logger.info("Маскировка номера карты начата")
        for i in range(0, len(masked_cardnumber), 4):
            masked_cardnumber_list.append(masked_cardnumber[i : i + 4])

        masked_card = " ".join(masked_cardnumber_list)
        logger.info("Маскировка номера карты успешна")
        return masked_card
    except Exception as e:
        logger.error(f"Ошибка маскировки номера карты: {e}")


def mask_account(account: str) -> str:
    """Функция, маскирующая номер счета"""
    try:
        logger.info("Маскировка номера счета начата")
        result = "**" + account[-4:]
        logger.info("Маскировка номера счета успешна")
        return result
    except Exception as e:
        logger.error(f"Ошибка маскировки номера счета: {e}")
