import pytest

from tasks.hard.factorial import factorial


@pytest.mark.parametrize(
    "n, expected", [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
    ]
)
def test_factorial(n, expected):
    assert factorial(n) == expected
