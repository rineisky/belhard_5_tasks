import pytest

from tasks.medium.sum_numbers import num_sum


@pytest.mark.parametrize(
    "n, expected", [
        (5216, 14),
        (58716, 27),
        (321, 6),
    ]
)
def test_num_sum(n, expected):
    assert num_sum(n) == expected
