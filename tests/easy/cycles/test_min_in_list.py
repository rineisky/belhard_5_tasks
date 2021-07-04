from tasks.easy.cycles.min_in_list import min_in_list


def test_min_in_list():
    assert min_in_list([-1, 5, -2, 3, -7, 8]) == -7
    assert min_in_list([-1, 5, -2, 3, -7, -8]) == -8
    assert min_in_list([-10, 5, -2, 3, -7, -8]) == -10
