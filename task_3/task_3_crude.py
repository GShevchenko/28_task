# Министерство обороны готовит группу элитных десантников, которые должны в кратчайший срок захватить тренировочный полигон "Квадраты". Территория Квадратов представляет собой прямоугольник из NxM квадратных областей, где каждая область имеет координаты 1 .. N , 1 .. M.
#
# Десантники в день 1 высаживаются в L областей, заданных их координатами (x1, y1), (x2,y2), ... , (xl, yl), которые считаются захваченными. На следующий день (день 2) они захватывают все соседние области, прилегающие к этим областям с четырёх сторон (по вертикали и горизонтали), и далее каждый следующий день этот процесс повторяется, пока не будут взяты под контроль все области без исключения.
#
# Генштаб требует точный план захвата плацдарма "Квадраты" -- на какой день он будет полностью контролироваться десантниками.
#
# Например:
#
#
#
# В первый день под контроль взяты две области (заштрихованы); во второй -- 8 областей (две с первого дня, сплошные синие, и шесть в текущий день, заштрихованы).
# В третий день (результирующее значение -- 3) вся территория тренировочного плацдарма оказывается под контролем десантников.
#
# Функция
#
# int ConquestCampaign(int N, int M, int L, int [] battalion)
# получает первыми двумя параметрами размер плацдарма "Квадраты" NxM, а battalion содержит массив из L*2 целых чисел (L >= 1) с индексацией с нуля, в котором каждый чётный (с чётным индексом) элемент содержит очередную координату области высадки по первому измерению N, а каждый нечётный (с нечётным индексом) элемент содержит очередную координату области высадки по второму измерению M.
# Не исключено, что в связи с неразберихой в командовании координаты областей высадки могут дублироваться.
# На примере с картинки параметры будут такими: N = 3, M = 4, L = 2, battalion = [2,2, 3,4]
#
# Возвращает функция день, начиная с 1, когда все области будут взяты под контроль.



from typing import List
import logging
import time


# Если ячейка открыта не сегодня, надо заполнить ее соседей и увеличить счетчик заполненных соседей на 1
def ConquestCampaign(N: int, M: int, L: int, battalion: List[int]) -> int:
    days = 1
    matrix = init_matrix(N, M, L, battalion)
    total_filled = int(len(battalion) / 2)
    while total_filled < M * N:
        logging.info("---------------------------------------")
        logging.info("Day is: %i", days)
        filled_today = []
        for y in range(N):
            interim = matrix[y]
            for x in range(M):
                if interim[x] == 1 and [y, x] not in filled_today:
                    filled_today.append([y, x])
                    total_filled += fill_neighbors(matrix, y, x, filled_today)
        print_matrix(matrix)
        time.sleep(2)
        logging.info("---------------------------------------")
        days += 1
    return days


# Открыть соседей - сверху, снизу, слева и справа.
# Если ячейка не открыта, открыть ее и добавить в списоок открытых сегодня ячеек и
# увеличить счетчик откытых ячеек на 1. Если открыта - пропустить.
def fill_neighbors(seeds: List[List[int]], y: int, x: int, filled_today: list[[int, int]]):
    count_filled_neighbors = 0
    logging.info("Fill neighbors for: y: %d, x: %d", y, x)
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
    logging.info("Were filled %i neighbors", count_filled_neighbors)
    return count_filled_neighbors


def init_matrix(size_y: int, size_x: int, seed_count: int, seeds: list[int]) -> list[list[int]]:
    matrix = []
    for i in range(size_y):
        interim = []
        for j in range(size_x):
            interim.append(0)
        matrix.append(interim)
    for i in range(0, seed_count * 2, 2):
        matrix[seeds[i] - 1][seeds[i + 1] - 1] = 1
    return matrix


def print_matrix(matrix: list[list[int]]):
    for i in range(len(matrix)):
        interim = matrix[i]
        logging.warning(interim)
        print()
    return matrix


logging.basicConfig(level=logging.WARN, format="")
days_result = ConquestCampaign(3, 4, 2, [2, 2, 3, 4])
logging.warning("Days is: " + str(days_result))
