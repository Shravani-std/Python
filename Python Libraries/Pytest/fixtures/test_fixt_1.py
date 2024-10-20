import pytest

@pytest.fixture
def sample_nums():
    return [1,2,3,4,5]

def test_sum(sample_nums):
    assert sum(sample_nums) == 15

def multiplication(sample_nums):
    result = 1
    for nums in sample_nums:
        result *= nums
    return result

def test_multiplication(sample_nums):
    assert multiplication(sample_nums) == 120