import pytest
from string_calculator import StringCalculator, StringCalculatorFactory


@pytest.fixture
def calculator() -> StringCalculator:
    """Fixture for StringCalculator."""
    return StringCalculatorFactory().default()


def test_empty_string(calculator: StringCalculator):
    assert calculator.calculate("") == 0


def test_single_number(calculator: StringCalculator):
    assert calculator.calculate("1") == 1


def test_two_numbers(calculator: StringCalculator):
    assert calculator.calculate("1,2") == 3


def test_multiple_numbers(calculator: StringCalculator):
    assert calculator.calculate("1,2,3,4,5") == 15


def test_newlines_as_separators(calculator: StringCalculator):
    assert calculator.calculate("1\n2,3") == 6


def test_custom_delimiter(calculator: StringCalculator):
    assert calculator.calculate("//;\n1;2") == 3


def test_negative_numbers(calculator: StringCalculator):
    with pytest.raises(ValueError) as excinfo:
        calculator.calculate("1,-2,3,-4")
    assert "negatives not allowed: -2, -4" in str(excinfo.value)


def test_ignore_over_1000(calculator: StringCalculator):
    assert calculator.calculate("2,1001") == 2


def test_longer_delimiter(calculator: StringCalculator):
    assert calculator.calculate("//[***]\n1***2***3") == 6


def test_multiple_delimiters(calculator: StringCalculator):
    assert calculator.calculate("//[*][%]\n1*2%3") == 6


def test_multiple_long_delimiters(calculator: StringCalculator):
    assert calculator.calculate("//[**][%%]\n1**2%%3") == 6



