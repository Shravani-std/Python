import pytest

def cal_square(x):
    return x * x

@pytest.mark.parametrize(" test_input, expected_output",
                         [
                             (5,25),
                             (8,64),
                             (9,81),
                             (10,100)
                         ])
def test_cal_square( test_input, expected_output):
    result = cal_square(test_input)
    assert result == expected_output



#instead of writing this many cases we have used above method
"""def test_cal_square_1():
    result = mathex.cal_square(5)
    assert result == 25
def test_cal_square_2():
    result = mathex.cal_square(8)
    assert result == 64

def test_cal_square_3():
    result = mathex.cal_square(9)
    assert result == 81

def test_cal_square_4():
    result = mathex.cal_square(10)
    assert result == 100
"""
