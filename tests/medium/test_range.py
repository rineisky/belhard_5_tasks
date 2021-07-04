from tasks.medium.range import list_compose


def test_list_compose():
    assert list_compose(
        [1, -1, 6, -12, 2, 3, 9, 4],
        ['a', 'b', 'c', 'd', 'e', 'f']
    ) == ['b', 'f', None, None, 'c', 'd', None, 'e']
