from FibArray import FibArray
from FibBinet import FibBinet
from FibEvenOdd import FibEvenOdd
from FibLoop import FibLoop
from FibRecursive import FibRecursive


import tkinter as tk
from tkinter import messagebox
import time
import math


class FibRecursive:
    @staticmethod
    def calculate(n):
        if n <= 1:
            return n
        return FibRecursive.calculate(n - 1) + FibRecursive.calculate(n - 2)

class FibLoop:
    @staticmethod
    def calculate(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

class FibArray:
    @staticmethod
    def calculate(n):
        fibs = [0] * (n + 1)
        fibs[0], fibs[1] = 0, 1
        for i in range(2, n + 1):
            fibs[i] = fibs[i - 1] + fibs[i - 2]
        return fibs

class FibBinet:
    @staticmethod
    def calculate(n):
        phi = (1 + math.sqrt(5)) / 2
        psi = (1 - math.sqrt(5)) / 2
        return round((phi ** n - psi ** n) / math.sqrt(5))

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


class FibonacciApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Вычисление чисел Фибоначчи")
        self.root.geometry("400x400+800+200")


        tk.Label(root, text="Введите n (1 ≤ n ≤ 64):").pack()
        self.entry = tk.Entry(root)
        self.entry.pack()


        self.selected_algorithm = tk.StringVar(value="Recursive")
        tk.Radiobutton(root, text="Рекурсивный", variable=self.selected_algorithm, value="Recursive").pack()
        tk.Radiobutton(root, text="Итеративный", variable=self.selected_algorithm, value="Loop").pack()
        tk.Radiobutton(root, text="Массив", variable=self.selected_algorithm, value="Array").pack()
        tk.Radiobutton(root, text="Формула Бине", variable=self.selected_algorithm, value="Binet").pack()
        tk.Radiobutton(root, text="Четность", variable=self.selected_algorithm, value="Even/Odd").pack()


        tk.Button(root, text="Вычислить", command=self.calculate).pack()

    def calculate(self):
        try:
            n = int(self.entry.get())
            if n < 1:
                raise ValueError("Число должно быть больше 0.")

            start_time = time.time()
            algorithm = self.selected_algorithm.get()

            if algorithm == "Recursive":
                result = FibRecursive.calculate(n)
            elif algorithm == "Loop":
                result = FibLoop.calculate(n)
            elif algorithm == "Array":
                result = FibArray.calculate(n)
            elif algorithm == "Binet":
                result = FibBinet.calculate(n)
            elif algorithm == "Even/Odd":
                result = FibEvenOdd.calculate(n)
            else:
                raise ValueError("Выберите алгоритм.")

            elapsed_time = (time.time() - start_time) * 1000  # Время в миллисекундах
            messagebox.showinfo("Результат", f"Результат: {result}\nВремя выполнения: {elapsed_time:.2f} мс")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciApp(root)
    root.mainloop()