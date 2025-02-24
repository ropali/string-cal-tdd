import re


class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        if len(numbers) == 1:
            return int(numbers)

        delimiters = [",", "\n"]

        # Check for custom delimiter
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)

            # Handle multiple delimiters in brackets
            if "[" in delimiter_line:
                # Extract all delimiters using regex
                custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_line)
                delimiters.extend(custom_delimiters)
            else:
                # Single custom delimiter without brackets
                delimiters.append(delimiter_line[2:])

        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ",")

        nums = [int(num) for num in numbers.split(",")]

        negatives = [num for num in nums if num < 0]

        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")

        nums = [num for num in nums if num <= 1000]

        return sum(nums)
