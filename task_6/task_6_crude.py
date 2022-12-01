import logging


def PatternUnlock(N: int, hits: list[int]) -> str:
    delta_1 = 1.00000
    delta_2 = 2**0.5
    displacement = 0
    for i in range(N - 1):
        logging.debug("Result is: %2.5d", displacement)
        if abs(hits[i] - hits[i + 1]) == 1 or hits[i] + hits[i + 1] == 10 or hits[i] + hits[i + 1] == 7:
            logging.debug("First if. i : %d", i)
            displacement += delta_1
        else:
            logging.debug("Second if. i : %d", i)
            displacement += delta_2
    result = ""
    logging.debug("Displacement is: %.5d", displacement)
    for c in str(round(displacement, 5)):
        logging.debug("Char is: %s", c)
        if c == '0' or c == ".":
            continue
        result += c
    return result



logging.basicConfig(level=logging.DEBUG, format="")
hist = [1, 2, 3, 4, 5, 6, 2, 7, 8, 9]
result = PatternUnlock(len(hist), hist)
logging.debug("Result is: %s", result)
logging.info("------------------------------------------------------")
logging.info(round(1.00000, 5))
logging.info(2**0.5)
logging.info(round(2**0.5, 5))