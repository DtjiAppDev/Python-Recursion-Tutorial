"""
This file contains implementation of calculating the sum of elements in a list using recursion.
Author: CreativeCloudAppDev2020
"""


from decimal import Decimal


def is_number(string: str) -> bool:
    try:
        Decimal(string)
        return True
    except:
        return False


def sum_of_list(a_list: list) -> Decimal:
    if len(a_list) == 0:
        return Decimal("0")
    elif len(a_list) == 1:
        if is_number(str(a_list[0])):
            return Decimal(a_list[0])
        else:
            return Decimal("0")
    else:
        if is_number(str(a_list[0])):
            return Decimal(a_list[0]) + sum_of_list(a_list[1:])
        else:
            return Decimal("0") + sum_of_list(a_list[1:])


# Test code

print(sum_of_list([4, 3, "5.17", "3.22s"]))  # 12.17
print(sum_of_list(["4.132", "5435.34243254325", "3234324.321432153425", "ssd", "xwt", 5]))  # 3239768.795864696675
