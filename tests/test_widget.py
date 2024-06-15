from src.widget import mask_account_card, get_data
import pytest


@pytest.mark.parametrize("x, expected", [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                         ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                                         ('Счет 35383033474447895560', 'Счет **5560'),
                                         ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                         ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                                         ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
                                         ('Счет 73654108430135874305', 'Счет **4305'),
                                         ('Счет 64686473678894779589', 'Счет **9589')])
def test_mask_account_card(x, expected):
    assert mask_account_card(x) == expected

# def test_get_data():
#     assert get_data()
