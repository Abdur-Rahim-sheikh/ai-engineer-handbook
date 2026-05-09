import pytest
from stuff.accum import Accumulator


def test_accumulator_init():
    acc = Accumulator()
    assert acc.count == 0


def test_accumulator_add():
    acc = Accumulator()
    acc.add()
    assert acc.count == 1
    acc.add(2)
    assert acc.count == 3


def test_cannot_set_directly():
    acc = Accumulator()
    with pytest.raises(AttributeError):
        acc.count = 10
