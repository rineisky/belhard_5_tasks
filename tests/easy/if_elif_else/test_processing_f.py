import pytest

from tasks.easy.if_elif_else.processing_f import processing_f


@pytest.mark.parametrize(
    "str_with_f, expected", [
        ("Hello World", "hELLO wORLD"),
        ("hi-fi acoustic", 3),
        ("fast forward", 5),
        ("finish false fox", "xof eslaf hsinif"),
    ]
)
def test_processing_f(str_with_f, expected):
    assert processing_f(str_with_f) == expected
