from tasks.easy.cycles.cycle_else import lets_else


def test_lets_else():
    assert lets_else(10) == 7
    assert lets_else(3) == -5
