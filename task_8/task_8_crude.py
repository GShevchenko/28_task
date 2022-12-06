import logging

def SumOfThe(N: int, data: list[int]) -> int:
    result: int = int(sum(data) / 2)
    return result


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')
data = [10, -25, -45, -35, 5]
res = SumOfThe(len(data), data)
logging.debug("Result is: %i", res)