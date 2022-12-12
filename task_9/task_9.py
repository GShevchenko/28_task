"""Задача 9"""
import math


def TheRabbitsFoot(s: str, encode: bool) -> str:
    """Метод кодировки-декодировки"""
    if encode:
        return make_encode(s)
    return make_decode(s)


def make_encode(data: str) -> str:
    """Метод для кодирования"""
    data_without_space: str = data.replace(" ", "")
    size: int = len(data_without_space)
    crude_size: float = size ** 0.5
    row_count: int = math.floor(crude_size)
    column_count: int = math.ceil(crude_size)
    while row_count * column_count < size:
        row_count += 1
    medium_matrix: list[str] = []
    for i in range(0, row_count):
        medium_matrix.append(data_without_space[i * row_count: (i + 1) * row_count])
    result: str = ""
    for i in range(column_count):
        for j in range(row_count):
            try:
                result += medium_matrix[j][i]
            except IndexError:
                continue
        result += " "
    return result


def make_decode(encoded_str: str) -> str:
    """Метод для декодирования"""
    result: str = ''
    encoded_arr: list[str] = encoded_str.split(" ")
    for i in range(len(encoded_arr[0])):
        for j in range(len(encoded_arr)):
            try:
                result += encoded_arr[j][i]
            except IndexError:
                continue
        result += " "
    return result.strip()
