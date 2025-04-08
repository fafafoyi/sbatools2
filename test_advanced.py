import pytest
from calculator import multiply, divide, is_even, power

# Fixture
@pytest.fixture
def sample_numbers():
    return 6, 2

def test_multiply(sample_numbers):
    a, b = sample_numbers
    assert multiply(a, b) == 12

def test_divide(sample_numbers):
    a, b = sample_numbers
    assert divide(a, b) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# Parameterized test
@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
])
def test_is_even(n, expected):
    assert is_even(n) == expected

@pytest.mark.parametrize("base, exp, result", [
    (2, 3, 8),
    (5, 0, 1),
    (3, 2, 9),
])
def test_power(base, exp, result):
    assert power(base, exp) == result
