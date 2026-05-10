import pytest


@pytest.mark.accumulator
def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add(accum):
    accum.add()
    assert accum.count == 1
    accum.add(2)
    assert accum.count == 3


def test_cannot_set_directly(accum):
    with pytest.raises(AttributeError):
        accum.count = 10
