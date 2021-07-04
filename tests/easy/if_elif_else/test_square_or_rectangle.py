import pytest

from tasks.easy.if_elif_else.square_or_rectangle import square_or_rectangle


@pytest.mark.parametrize(
    "side1, side2, expected", [
        (6, 10, 32),
        (4, 4, 16),
    ]
)
def test_square_or_rectangle(side1, side2, expected):
    assert square_or_rectangle(side1, side2) == expected
