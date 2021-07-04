import pytest

from tasks.easy.if_elif_else.replacer import replacer


@pytest.mark.parametrize(
    "check_str, search_str, replace_str, expected", [
        ("как у тебя дела", "у тебя", "твои", "Как твои дела"),
        ("что делаешь", "ты", "мы", "Ошибка!"),
    ]
)
def test_replacer(check_str, search_str, replace_str, expected):
    assert replacer(check_str, search_str, replace_str) == expected
