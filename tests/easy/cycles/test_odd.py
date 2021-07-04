from tasks.easy.cycles.odd import odd_in_list


def test_odd_in_list():
    assert odd_in_list([1, False, 2, -1, 'Hi', 4, 6, [], (), -8]) == [2, 4, 6, -8]
    assert odd_in_list([2, -1, 4, True, None, 6]) == [2, 4, 6]
