from typing import Generator
import random as r

#### Should generate a dictionary of
#### - 8 digits (only `chiffres`)
#### - No double allowed

_dict = []

x = 0

def string_generator(size: int = 1, amount: int = 1) -> Generator[str, None, None]:
    """
    Return x random strings of a fixed length.

    :param size: string length, defaults to 1
    :type size: int, optional
    :param amount: amount of random strings to generate, defaults to 1
    :type amount: int, optional
    :yield: Yield composed random string if unique
    :rtype: Generator[str, None, None]
    """
    CHARS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    LIMIT = len(CHARS) ** size
    count, check, string = 0, set(), ''
    while LIMIT > count < amount:
        string = ''.join(r.choices(CHARS, k=size))
        if string not in check:
            check.add(string)
            yield string
            count += 1

_dict = string_generator(8, 1814400)
print("Recursion done")
with open("./brutedict.txt", "wt", encoding="utf-8") as fout:
  for _string in _dict:
    fout.write(_string + "\n")