import pytest

from tasks.medium.leap_year import is_year_leap


@pytest.mark.parametrize(
    "year, expected", [
        (1700, False),
        (1800, False),
        (1900, False),
        (2100, False),
        (1988, True),
        (1600, True),
        (2400, True),
    ]
)
def test_is_year_leap(year, expected):
    assert is_year_leap(year) == expected
