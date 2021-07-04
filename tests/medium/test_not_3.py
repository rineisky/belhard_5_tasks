import pytest

from tasks.medium.not_3 import not_3


@pytest.mark.parametrize(
    "array, expected", [
        ([2, 1, 3, 5, 6, 4, 7], [2, 1, 5, 4, 7]),
        ([6, 2, 3, 4, 1, 7], [2, 4, 1, 7]),
    ]
)
def test_not_3(array, expected):
    assert not_3(array) == expected
