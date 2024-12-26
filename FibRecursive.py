class FibRecursive:
    @staticmethod
    def calculate(n):
        if n <= 1:
            return n
        return FibRecursive.calculate(n - 1) + FibRecursive.calculate(n - 2)