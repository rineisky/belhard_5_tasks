import pytest

from tasks.hard.most_common_and_longest import common_and_longest


@pytest.mark.parametrize(
    "text, expected", [
        ("привет компилляция генерация привет код", ("привет", "компилляция")),
        ("а б в с б цбб ф б", ("б", "цбб")),
    ]
)
def test_common_and_longest(text, expected):
    assert common_and_longest(text) == expected
