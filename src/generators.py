# card_number_generator
def cardnumber_generator(start, end):
    for number in range(start, end + 1):
        yield f"{number:016d}".replace("", " ").strip()

def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]


def filter_by_currency(transactions, currency):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


# Usage of card_number_generator
# print("\nCard Number Generator:")
# for cardnumber in cardnumber_generator(99999999799, 99999999999):
#     print(cardnumber)