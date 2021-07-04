import pytest

from tasks.easy.if_elif_else.find_and_replace import find_and_replace


@pytest.mark.parametrize(
    "check_str, search_str, expected", [
        ('Как твои дела', 'Как', ('кАК ТВОИ ДЕЛА', 'Как')),
        ('добРый день коЛЛеги', 'день', ('ДОБрЫЙ ДЕНЬ КОллЕГИ', 'День')),
        ('добРый день коЛЛеги', 'тень', ('добРый день коЛЛеги', 'тень')),
    ]
)
def test_find_and_replace(check_str, search_str, expected):
    assert find_and_replace(check_str, search_str) == expected
