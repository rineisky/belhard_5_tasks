import pytest

from tasks.easy.exceptions.odd_sum import odd_sum


def test_odd_sum():
    with pytest.raises(TypeError):
        odd_sum([1, False, 2, -1, 'Hi', 4, 6, [], (), -8])

    assert odd_sum([1, 2, 3, 4, 5, 6]) == 9
