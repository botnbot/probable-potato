from src.masks import mask_card_number, mask_account
import pytest


def test_mask_card_number():
    assert mask_card_number('1234567812345678') == '1234 56** **** 5678'


# def test_mask_card_number_fail():
#     with pytest.raises(ValueError):
#         mask_card_number('0')

def test_mask_account():
    assert mask_account('12345678901234567890') == '**7890'
#
