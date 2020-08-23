"""
This file contains implementation of calculating the sum of first n positive integers using recursion.
Author: CreativeCloudAppDev2020
"""


def calculate_sum_first_n(n: int) -> int:
    if n < 0:
        return 0
    elif n == 0:
        return 0
    else:
        return n + calculate_sum_first_n(n - 1)


# Test code

print(calculate_sum_first_n(50))  # 1275
print(calculate_sum_first_n(5))  # 15
print(calculate_sum_first_n(-1))  # 0
