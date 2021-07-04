import pytest

from tasks.hard.insertion_sort import insertion_sort


@pytest.mark.parametrize(
    "before, after", [
        ([2, 1, 5, 4, 7], [1, 2, 4, 5, 7]),
        ([2, -5, -3, 3, 1, 2], [-5, -3, 1, 2, 2, 3]),
        ([2, 2, -3, 3, 1, -5], [-5, -3, 1, 2, 2, 3]),
    ]
)
def test_insertion_sort(before, after):
    assert insertion_sort(before) == after
