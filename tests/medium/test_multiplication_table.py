import pytest

from tasks.medium.multiplication_table import multiplication_table


@pytest.mark.parametrize(
    "n, expected", [
        (5, [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]),
        (2, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),
        (3, [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]),
    ]
)
def test_multiplication_table(n, expected):
    assert multiplication_table(n) == expected
