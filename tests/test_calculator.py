import os
import sys
import pytest

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from calculator import add, divide, factorial, multiply


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_factorial_positive_number():
    assert factorial(5) == 120


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_negative_number():
    with pytest.raises(ValueError):
        factorial(-1)


def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_multiply_with_negative_number():
    assert multiply(3, -4) == -12
