from src.masks import mask_card_number, mask_account
import pytest


@pytest.fixture
def my_string():
    return '1234567812345678'
def test_mask_card_number(my_string):
    assert mask_card_number(my_string) == '1234 56** **** 5678'


def test_mask_account(my_string):
    assert mask_account(my_string) == '**5678'
