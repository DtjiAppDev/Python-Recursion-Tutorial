"""
This file contains implementation of counting the number of digits in a string using recursion.
Author: CreativeCloudAppDev2020
"""


digits: str = "0123456789"


def count_number_of_digits(string: str) -> int:
    return count_number_of_digits_aux(string, 0, 0)


def count_number_of_digits_aux(string: str, index: int, sum: int) -> int:
    if index == len(string):
        return sum
    else:
        if str(string[index]) in digits:
            return count_number_of_digits_aux(string, index + 1, sum + 1)
        return count_number_of_digits_aux(string, index + 1, sum)


# Test code

print(count_number_of_digits("ssd72746382dsffsgd"))  # 8
print(count_number_of_digits("b40 jidofhjasd2"))  # 3
print(count_number_of_digits("ssd7834875hasfafd23424f32rf"))  # 14
