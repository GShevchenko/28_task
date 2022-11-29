def SynchronizingTables(N: int, ids: list[int], salary: list[int]) -> list[int]:
    ids_copy = []
    for i in ids:
        ids_copy.append(i)
    ids_dict = {}
    for i in range(len(ids_copy)):
        ids_dict[ids_copy[i]] = i
    sort_array(ids_copy)
    sort_array(salary)
    salary_dict = {}
    for i in range(len(ids_copy)):
        salary_dict[salary[i]] = ids_dict[ids_copy[i]]
    for k, v in salary_dict.items():
        salary[v] = k
    return salary


def sort_array(some_arr: list[int]):
    for i in range(len(some_arr) - 1):
        m = i
        for j in range(i + 1, len(some_arr)):
            if some_arr[j] <= some_arr[m]:
                m = j
        some_arr[m], some_arr[i] = some_arr[i], some_arr[m]
