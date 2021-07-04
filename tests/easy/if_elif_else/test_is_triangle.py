import pytest

from tasks.easy.if_elif_else.is_triangle import is_triangle


@pytest.mark.parametrize(
    "side1, side2, side3, expected", [
        (3, 4, 5, True),
        (10, 4, 5, False),
    ]
)
def test_is_triangle(side1, side2, side3, expected):
    assert is_triangle(side1, side2, side3) == expected
