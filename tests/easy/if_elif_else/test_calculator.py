import pytest

from tasks.easy.if_elif_else.calculator import calculator


@pytest.mark.parametrize(
    "a, b, operation, result", [
        (2, 3, '+', 5),
        (2, 3, '-', -1),
        (2, 3, '*', 6),
        (2, 3, '/', 2 / 3),
        (2, 3, 'no', "Неизвестная операция"),
    ]
)
def test_calculator(a, b, operation, result):
    assert calculator(a, b, operation) == result
