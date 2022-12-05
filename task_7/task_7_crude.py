import logging
import re


def WordSearch(length: int, s: str, subs: str) -> list[int]:
    result = []
    strings = split(s, length)
    logging.debug("---------------------------------")
    logging.debug("Splitted string is: %s", strings)
    for i in strings:
        if len(re.findall('\\b' + subs + '\\b', i)) > 0:
            result.append(1)
        else:
            result.append(0)
    return result


def split(long_string: str, length: int) -> list[str]:
    resulted_strings = []
    splitted_strings = long_string.split(" ")
    if len(splitted_strings) == 0:
        splitted_strings.append(long_string)
    size = len(splitted_strings)
    i = 0
    while i < size:
        logging.info("Start i is: %i", i)
        if splitted_strings[i] == " " or splitted_strings[i] == "":
            i += 1
            continue
        if len(splitted_strings[i]) == length:
            resulted_strings.append(splitted_strings[i])
            i += 1
            continue
        if len(splitted_strings[i]) < length:
            concat_str = splitted_strings[i]
            while i < size - 1 and len(concat_str) + len(splitted_strings[i + 1]) < length:
                i += 1
                concat_str = concat_str + " " + splitted_strings[i]
            # logging.debug("Concat str: %s, i: %i", concat_str, i)
            resulted_strings.append(concat_str)
            continue
        if len(splitted_strings[i]) > length:
            delta = 0
            while delta < len(splitted_strings[i]):
                resulted_strings.append(splitted_strings[i][delta:length + delta])
                delta += length
        logging.info("End i is: %i", i)
        i += 1
    return resulted_strings


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')
subs = 'строк'
my_string = '1) строка разбивается на набор строк через выравнивание по заданной ширине.'
# result = WordSearch(12, my_string, subs)
result1 = WordSearch(3, '123456123', '123')
# logging.debug(result)
logging.debug("Result is: %s", result1)
logging.debug(my_string[0:4])
