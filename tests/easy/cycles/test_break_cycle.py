import pytest

from tasks.easy.cycles.break_cycle import lets_break


def test_lets_break():
    assert lets_break(5) == 5
    assert lets_break(0) == 10
    assert lets_break(10) == 0

    with pytest.raises(ValueError):
        assert lets_break(20)
