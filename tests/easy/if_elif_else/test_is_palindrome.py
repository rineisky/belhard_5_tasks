import pytest

from tasks.easy.if_elif_else.is_palindrome import is_palindrome


@pytest.mark.parametrize(
    "check_str, expected", [
        ("дом мод", True),
        ("мадам", True),
        ("город дорог", True),
        ("привет", False),
    ]
)
def test_is_palindrome(check_str, expected):
    assert is_palindrome(check_str) == expected
