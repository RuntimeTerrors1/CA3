from app import add
from app import div
from app import mul

def test_add():
    assert 6 == add(4, 2)

def test_div():
    assert 2 == div(6,3)

def test_multiply():
    assert mul(2, 3) == 6
    assert mul(1, 2) == 2