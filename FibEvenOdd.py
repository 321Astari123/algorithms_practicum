class FibEvenOdd:
    @staticmethod
    def calculate(n):
        if n == 0:
            return "even"
        elif n == 1:
            return "odd"

        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, (a + b) % 10  # Сохраняем только последнюю цифру
        return "even" if b % 2 == 0 else "odd"