"""
This file contains implementation of calculating the nth Fibonacci number using recursion
Author: CreativeCloudAppDev2020
"""


def fibonacci(n: int) -> int:
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Test code
print(fibonacci(3))  # 2
print(fibonacci(4))  # 3
print(fibonacci(5))  # 5
