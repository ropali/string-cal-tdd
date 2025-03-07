import re
from abc import ABC, abstractmethod


class NumberParser(ABC):

    @abstractmethod
    def parse(self, numbers: str) -> list[int]:
        pass


class DefuaultNumberParser(NumberParser):
    def parse(self, numbers: str) -> list[int]:
        return [int(num) for num in numbers.split(",")]


class CustomDelimiterParser(NumberParser):
    def __init__(self):
        super().__init__()
        self.delimiters = ["\n"]

    def parse(self, numbers: str) -> list[int]:
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)

            if "[" in delimiter_line:
                custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_line)
                self.delimiters.extend(custom_delimiters)
            else:
                self.delimiters.append(delimiter_line[2:])

        for delimiter in self.delimiters:
            numbers = numbers.replace(delimiter, ",")

        return [int(num) for num in numbers.split(",")]


class OptimizedDelimiterParser(NumberParser):

    def __init__(self):
        super().__init__()
        self.delimiters = [",", "\n"]

    def parse(self, numbers):

        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)

            if "[" in delimiter_line:
                custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_line)
                self.delimiters.extend(custom_delimiters)
            else:
                self.delimiters.append(delimiter_line[2:])

        # create a regex pattern for all delimiters
        pattern = "|".join(map(re.escape, self.delimiters))

        nums = re.split(pattern, numbers)

        return [int(num) for num in nums]


class NumberValidator(ABC):
    @abstractmethod
    def validate(self, numbers: list[int]) -> None:
        pass


class NegativeNumberValidator(NumberValidator):
    def validate(self, numbers: list[int]) -> None:
        negatives = [num for num in numbers if num < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")


class NumberFilter(ABC):
    @abstractmethod
    def filter(self, numbers: list[int]) -> list[int]:
        pass


class IgnoreOverThousandFilter(NumberFilter):
    def filter(self, numbers: list[int]) -> list[int]:
        return [num for num in numbers if num <= 1000]


class Operation(ABC):
    @abstractmethod
    def calculate(self, numbers: list[int]) -> int:
        pass


class Addition(Operation):
    def calculate(self, numbers: list[int]) -> int:
        return sum(numbers)


class Subtraction(Operation):
    def calculate(self, numbers: list[int]) -> int:
        return numbers[0] - sum(numbers[1:])


class Multiplication(Operation):
    def calculate(self, numbers: list[int]) -> int:
        result = numbers[0]

        for num in numbers[1:]:
            result *= num
        return result


class Division(Operation):
    def calculate(self, numbers: list[int]) -> int:
        result = numbers[0]

        for num in numbers[1:]:
            if num == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result /= num
        return result


class StringCalculator:

    def __init__(
        self,
        operation: Operation,
        number_parser: NumberParser,
        number_validator: list[NumberValidator],
        number_filter: list[NumberFilter],
    ):
        self.operation = operation
        self.number_parser = number_parser
        self.number_validators = number_validator
        self.number_filters = number_filter

    def calculate(self, numbers: str) -> int:

        if not numbers:
            return 0

        numbers = self.number_parser.parse(numbers)

        for validator in self.number_validators:
            validator.validate(numbers)

        for filter in self.number_filters:
            numbers = filter.filter(numbers)

        return self.operation.calculate(numbers)


class StringCalculatorFactory:
    @staticmethod
    def default() -> StringCalculator:
        operation = Addition()
        number_parser = OptimizedDelimiterParser()
        number_validators = [NegativeNumberValidator()]
        number_filters = [IgnoreOverThousandFilter()]

        return StringCalculator(
            operation, number_parser, number_validators, number_filters
        )
