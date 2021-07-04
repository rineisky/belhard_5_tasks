import pytest

from tasks.easy.if_elif_else.is_divide_by import is_divide_by


@pytest.mark.parametrize(
    "to_divide, divider_1, divider_2, expected", [
        (-12, 2, -6, True),
        (45, 5, 15, True),
        (4, 1, 4, True),
        (15, -5, 3, True),
        (-12, 2, -5, False),
        (45, 1, 6, False),
    ]
)
def test_is_divide_by(to_divide, divider_1, divider_2, expected):
    assert is_divide_by(to_divide, divider_1, divider_2) == expected
