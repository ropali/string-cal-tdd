
class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        if len(numbers) == 1:
            return int(numbers)