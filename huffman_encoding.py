# 2.1. Кодирование строки по алгоритму Хаффмана
import heapq
from collections import Counter


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encode(text):
    # 1. Подсчет частоты символов
    frequency = Counter(text)

    # 2. Создание приоритетной очереди (кучи)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    # 3. Построение дерева Хаффмана
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    # 4. Генерация кодов Хаффмана
    huffman_codes = {}

    def generate_codes(node, current_code):
        if node is not None:
            if node.char is not None:
                huffman_codes[node.char] = current_code
            generate_codes(node.left, current_code + '0')
            generate_codes(node.right, current_code + '1')

    root = priority_queue[0]
    generate_codes(root, '')

    # 5. Кодирование строки
    encoded_text = ''.join(huffman_codes[char] for char in text)

    # 6. Вывод результатов в требуемом формате
    unique_chars_count = len(frequency)
    encoded_size = len(encoded_text)

    # Первая строка: количество уникальных символов и размер закодированной строки
    print(f"{unique_chars_count} {encoded_size}")

    # Следующие строки: коды символов в формате "'symbol': code"
    for char, code in sorted(huffman_codes.items()):
        print(f"'{char}': {code}")

    # Последняя строка: закодированная строка
    print(encoded_text)


# Ввод текста
text = "Errare humanum est."
huffman_encode(text)