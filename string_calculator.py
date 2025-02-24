
class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        if len(numbers) == 1:
            return int(numbers)
        

        delimiters = [",", "\n"]
        
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, ",")
        
        return sum(int(num) for num in numbers.split(","))