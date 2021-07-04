import pytest

from tasks.easy.if_elif_else.clock import get_seconds


@pytest.mark.parametrize(
    "h, m, s, expected", [
        (2, 13, 25, 8005),
        (23, 0, 43, 82843),
        (25, 0, 43, "Ошибка. Допустимое значение для часов 0..23"),
        (23, 61, 43, "Ошибка. Допустимое значение для минут 0..59"),
        (23, 0, -1, "Ошибка. Допустимое значение для секунд 0..59"),
    ]
)
def test_get_seconds(h, m, s, expected):
    assert get_seconds(h, m, s) == expected
