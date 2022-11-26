from typing import List


def ConquestCampaign(size_y: int, size_x: int, seed_count: int, seeds: List[int]) -> int:
    days = 1
    matrix = init_matrix(size_y, size_x, seed_count, seeds)
    total_filled = int(len(seeds) / 2)
    while total_filled < size_x * size_y:
        filled_today = []
        for y in range(size_y):
            interim = matrix[y]
            for x in range(size_x):
                if interim[x] == 1 and [y, x] not in filled_today:
                    filled_today.append([y, x])
                    total_filled += fill_neighbors(matrix, y, x, filled_today)
        days += 1
    return days


def fill_neighbors(seeds: List[List[int]], y: int, x: int, filled_today: list[[int, int]]):
    count_filled_neighbors = 0
    if y - 1 >= 0 and seeds[y - 1][x] != 1:
        seeds[y - 1][x] = 1
        filled_today.append([y - 1, x])
        count_filled_neighbors += 1
    if y + 1 < len(seeds) and seeds[y + 1][x] != 1:
        seeds[y + 1][x] = 1
        filled_today.append([y + 1, x])
        count_filled_neighbors += 1
    if x - 1 >= 0 and seeds[y][x - 1] != 1:
        seeds[y][x - 1] = 1
        filled_today.append([y, x - 1])
        count_filled_neighbors += 1
    if x + 1 < len(seeds[y]) and seeds[y][x + 1] != 1:
        seeds[y][x + 1] = 1
        count_filled_neighbors += 1
        filled_today.append([y, x + 1])
    return count_filled_neighbors


def init_matrix(size_y: int, size_x: int, seed_count: int, seeds: list[int]) -> list[list[int]]:
    matrix = []
    for i in range(size_y):
        interim = []
        for _ in range(size_x):
            interim.append(0)
        matrix.append(interim)
    for i in range(0, seed_count * 2, 2):
        matrix[seeds[i] - 1][seeds[i + 1] - 1] = 1
    return matrix
