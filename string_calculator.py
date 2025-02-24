
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
            delimiter = delimiter_line[2:]
            delimiters.append(delimiter)
            
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ",")

        
        nums = [int(num) for num in numbers.split(",")]

        negatives = [num for num in nums if num < 0]

        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
        
        nums = [num for num in nums if num <= 1000]
        
        return sum(nums)