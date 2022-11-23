from typing import List


def odometer(oksana: List[int]) -> int:
    total_path = oksana[0] * oksana[1]
    for i in range(2, len(oksana), 2):
        total_path += oksana[i] * (oksana[i + 1] - oksana[i - 1])
    return total_path
