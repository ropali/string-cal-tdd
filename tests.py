import pytest
from string_calculator import StringCalculator

def test_empty_string():
    calculator = StringCalculator()
    assert calculator.add("") == 0


def test_single_number():
    calculator = StringCalculator()
    assert calculator.add("1") == 1


def test_two_numbers():
    calculator = StringCalculator()
    assert calculator.add("1,2") == 3

    
def test_multiple_numbers():
    calculator = StringCalculator()
    assert calculator.add("1,2,3,4,5") == 15


def test_newlines_as_separators():
    calculator = StringCalculator()
    assert calculator.add("1\n2,3") == 6