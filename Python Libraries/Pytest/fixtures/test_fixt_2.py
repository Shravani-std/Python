import pytest

@pytest.fixture
def input():
    i = 12
    return i

def test_sqr(input):
    assert input*input == 144

def test_cube(input):
    assert input*input*input == 1728