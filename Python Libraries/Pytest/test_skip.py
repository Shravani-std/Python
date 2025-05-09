import pytest

def cal_sum(x,y):
    return x+y

def cal_multi(x,y):
    return x*y

@pytest.mark.skip(reason = "Unwanted")
def test_cal_sum():
    assert cal_sum(2,3) == 5

def test_cal_multi():
    assert cal_multi(2,3) == 6