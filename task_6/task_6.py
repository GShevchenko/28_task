def PatternUnlock(N: int, hits: list[int]) -> str:
    delta_1 = 1.00000
    delta_2 = 2**0.5
    displacement = 0
    for i in range(N - 1):
        if abs(hits[i] - hits[i + 1]) == 1 or hits[i] + hits[i + 1] == 10 or hits[i] + hits[i + 1] == 7:
            displacement += delta_1
        else:
            displacement += delta_2
    result = ""
    for c in str(round(displacement, 5)):
        if c == '0' or c == ".":
            continue
        result += c
    return result
