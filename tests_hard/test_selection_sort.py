import pytest

from tasks.hard.selection_sort import selection_sort


@pytest.mark.parametrize(
    "before, after", [
        ([2, 1, 5, 4, 7], [1, 2, 4, 5, 7]),
        ([2, -5, -3, 3, 1, 2], [-5, -3, 1, 2, 2, 3]),
        ([2, 2, -3, 3, 1, -5], [-5, -3, 1, 2, 2, 3]),
    ]
)
def test_selection_sort(before, after):
    assert selection_sort(before) == after
