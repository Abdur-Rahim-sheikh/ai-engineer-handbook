import pytest


@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2


# raises
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0


# parametrize
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 2),
        (2, 3, 6),
        (3, 4, 12),
        (0, 5, 0),
        (-1, 2, -2),
        (-2, -3, 6),
        # intentionally incorrect test case to demonstrate failure
        (2, 2, 5),
    ],
)
def test_multiply(a, b, expected):
    assert a * b == expected
