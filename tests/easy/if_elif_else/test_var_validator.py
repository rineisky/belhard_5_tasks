import pytest

from tasks.easy.if_elif_else.var_validator import is_valid


@pytest.mark.parametrize(
    "check_string, expected", [
        ("hello", True),
        ("123_pr", False),
        ("def", False),
    ]
)
def test_is_valid(check_string, expected):
    assert is_valid(check_string) == expected
