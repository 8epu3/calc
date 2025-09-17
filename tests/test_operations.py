import pytest
from calculator.operations import *

def test_add():
    assert add(3, 3) == 6
    assert add(0, -3) == -3

def test_sub():
    assert sub(3, 3) == 0
    assert sub(-2, 8) == -10

def test_mul():
    assert mul(3, 3) == 9
    assert mul(3, 0) == 0
    assert mul(-3, 3) == -9

def test_div():
    assert div(4, 2) == 2
    assert div(0, 3) == 0
    assert div(-4, 2) == -2

def test_div_by_zero():
    with pytest.raises(ValueError, match="Division by zero not allowed."):
        div(3, 0)