import pytest

from tasks.medium.unique_in_list import is_unique


@pytest.mark.parametrize(
    "array, expected", [
        ([2, 1, 5, 4, 7], True),
        ([2, 1, 5, 4, 2], False),
    ]
)
def test_is_unique(array, expected):
    assert is_unique(array) == expected
