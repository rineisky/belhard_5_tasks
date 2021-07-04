import pytest

from tasks.hard.bubble_sort import bubble_sort


@pytest.mark.parametrize(
    "before, after", [
        ([2, 1, 5, 4, 7], [1, 2, 4, 5, 7]),
        ([2, -5, -3, 3, 1, 2], [-5, -3, 1, 2, 2, 3]),
        ([2, 2, -3, 3, 1, -5], [-5, -3, 1, 2, 2, 3]),
    ]
)
def test_bubble_sort(before, after):
    assert bubble_sort(before) == after
