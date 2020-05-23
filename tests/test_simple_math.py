from tutorial import simple_math


def test_add():
    assert 5 == simple_math.add(2, 3)


def test_multiply():
    assert 10 == simple_math.multiply(2, 5)
