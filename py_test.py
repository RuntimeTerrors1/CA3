from app import add
from app import div

def test_add():
    assert 6 == add(4, 2)

def test_div():
    assert 2 == div(6,3)