import mathex

def test_cal_total():
    total = mathex.cal_total(5,5)
    assert total == 10

def test_cal_multi():
    result = mathex.cal_multi(5,5)
    assert result == 25