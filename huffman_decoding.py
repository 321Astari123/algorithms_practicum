# 2.2. Декодирование строки по алгоритму Хаффмана
def huffman_decode():
    header = "12 67"
    code_map = {
        'E': '0000',
        't': '0001',
        'e': '001',
        'u': '010',
        ' ': '011',
        'a': '100',
        's': '1010',
        'n': '1011',
        'r': '110',
        'm': '1110',
        '.': '11110',
        'h': '11111'
    }
    encoded_string = "0000110110100110001011111110101110100101101011100110011010000111110"

    reverse_map = {code: char for char, code in code_map.items()}

    decoded_string = ""
    buffer = ""
    for bit in encoded_string:
        buffer += bit
        if buffer in reverse_map:
            decoded_string += reverse_map[buffer]
            buffer = ""

    print(decoded_string)

huffman_decode()