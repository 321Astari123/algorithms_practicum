import math

class FibBinet:
    @staticmethod
    def calculate(n):
        phi = (1 + math.sqrt(5)) / 2
        psi = (1 - math.sqrt(5)) / 2
        return round((phi ** n - psi ** n) / math.sqrt(5))