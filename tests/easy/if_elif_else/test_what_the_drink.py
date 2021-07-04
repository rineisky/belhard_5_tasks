import pytest

from tasks.easy.if_elif_else.what_the_drink import what_you_drink


@pytest.mark.parametrize(
    "age, expected", [
        (13, "можно сок"),
        (17, "можно кока-колу"),
        (18, "можно пиво"),
        (20, "можно пиво"),
        (30, "можно виски"),
    ]
)
def test_what_you_drink(age, expected):
    assert what_you_drink(age) == expected
