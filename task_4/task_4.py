def MadMax(N: int, Tele: list[int]) -> list[int]:
    sort_array(Tele)
    reformate_sorted_array(Tele)
    return Tele


def reformate_sorted_array(some_arr: list[int]):
    l = len(some_arr)
    half_l = int(l / 2) + 1
    for i in range(int(half_l / 2)):
        some_arr[half_l + i - 1], some_arr[l - i - 1] = \
            some_arr[l - i - 1], some_arr[half_l + i - 1]


def sort_array(some_arr: list[int]):
    for i in range(len(some_arr) - 1):
        m = i
        for j in range(i + 1, len(some_arr)):
            if some_arr[j] <= some_arr[m]:
                m = j
        some_arr[m], some_arr[i] = some_arr[i], some_arr[m]
