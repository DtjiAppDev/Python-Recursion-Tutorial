"""
This file contains implementation of a recursive list.
Author: CreativeCloudAppDev2020
"""


class RecursiveList(object):
    """
    This class contains attributes of a recursive list.
    """

    class EmptyList(object):
        """
        An empty list
        """

        def __len__(self) -> int:
            return 0

    empty: EmptyList = EmptyList()

    def __init__(self, first, rest=empty):
        # type: (object, RecursiveList) -> None
        self.first: object = first
        self.rest: RecursiveList or RecursiveList.EmptyList = rest

    def append(self, other: object) -> None:
        if isinstance(self.rest, RecursiveList.EmptyList):
            self.rest = RecursiveList(other)
            return
        self.rest.append(other)

    def remove(self, instance: object) -> None:
        if self.first == instance:
            self.first = self.rest.first
            self.rest = self.empty if isinstance(self.rest, RecursiveList.EmptyList) else self.rest.rest
            return
        else:
            if isinstance(self.rest, RecursiveList.EmptyList):
                return
            self.rest.remove(instance)

    def __str__(self):
        # type: () -> str
        return self.str_aux("[")

    def str_aux(self, accumulated: str) -> str:
        if isinstance(self.rest, RecursiveList.EmptyList):
            accumulated += str(self.first) + "]"
            return accumulated
        else:
            accumulated += str(self.first) + ", "
            assert isinstance(self.rest, RecursiveList), "Sorry, invalid argument self.rest. self.rest should be a " \
                                                         "Recursive List"
            return self.rest.str_aux(accumulated)

    def __len__(self) -> int:
        return 1 + len(self.rest)

    def __getitem__(self, i: int) -> object:
        if i == 0:
            return self.first
        return self.rest[i - 1]


# Test code

recursive_list: RecursiveList = RecursiveList(1, RecursiveList(2, RecursiveList(3)))
print(recursive_list)  # [1, 2, 3]
print(len(recursive_list))  # 3
print(recursive_list[2])  # 3
recursive_list.append(5)
print(recursive_list)  # [1, 2, 3, 5]
print(len(recursive_list))  # 4
print(recursive_list[0])  # 1
recursive_list.remove(4)
print(recursive_list)  # [1, 2, 3, 5]
print(len(recursive_list))  # 4
print(recursive_list[3])  # 5
recursive_list.remove(3)
print(recursive_list)  # [1, 2, 5]
print(len(recursive_list))  # 3
print(recursive_list[1])  # 2
recursive_list.append(7)
print(recursive_list)  # [1, 2, 5, 7]
print(len(recursive_list))  # 4
print(recursive_list[3])  # 7
