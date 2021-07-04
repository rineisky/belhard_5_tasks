import pytest

from tasks.easy.if_elif_else.equation import resolve_equation


@pytest.mark.parametrize(
    "a, b, c, expected", [
        (1, -2, -3, (16, 2, 3, -1)),
        (-1, -2, 15, (64, 2, -5, 3)),
        (1, 12, 36, (0, 1, -6, None)),
    ]
)
def test_resolve_equation(a, b, c, expected):
    assert resolve_equation(a, b, c) == expected
