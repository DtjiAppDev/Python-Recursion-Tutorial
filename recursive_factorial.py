"""
This file contains implementation of calculating the factorial of an integer using recursion
Author: CreativeCloudAppDev2020
"""


def factorial(n: int) -> int:
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Test code

print(factorial(5))  # 120
print(factorial(4))  # 24
print(factorial(5) * 6 == factorial(6))  # True
print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(-1))  # 0
