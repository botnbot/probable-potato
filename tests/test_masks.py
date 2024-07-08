import pytest


from src.masks import mask_card_number, mask_account


@pytest.fixture
def number():
    return "1234567812345678"


def test_mask_card_number(number):
    assert mask_card_number(number) == "1234 56** **** 5678"


def test_mask_account(number):
    assert mask_account(number) == "**5678"
