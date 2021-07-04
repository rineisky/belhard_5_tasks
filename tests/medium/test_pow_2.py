import pytest

from tasks.medium.pow_2 import is_pow_2


@pytest.mark.parametrize(
    "n, expected", [
        (1, True),
        (2, True),
        (16, True),
        (256, True),
        (1024, True),
        (13, False),
        (17, False),
    ]
)
def test_is_pow_2(n, expected):
    assert is_pow_2(n) == expected
