import pytest

from tasks.easy.if_elif_else.payment_card import hide_card_numbers


@pytest.mark.parametrize(
    "card_number, expected", [
        ("1234567891123456", "1234********3456"),
        ("123privet123", "Ошибка"),
    ]
)
def test_hide_card_numbers(card_number, expected):
    assert hide_card_numbers(card_number) == expected
