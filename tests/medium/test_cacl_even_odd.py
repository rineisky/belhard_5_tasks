import pytest

from tasks.medium.calc_even_odd import calc_even_odd


@pytest.mark.parametrize(
    "array, expected", [
        ([2, 1, 5, 4, 7], (2, 3)),
        ([2, -5, -3, 3, 1, 2], (2, 4)),
    ]
)
def test_calc_even_odd(array, expected):
    assert calc_even_odd(array) == expected
