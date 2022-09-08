from sources.reverse import reverse, max, reverse_sort
from copy import deepcopy


def is_reverse_sorted(lst: list) -> bool:
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True


class TestReverseAlgorithm:
    long_long_initial_list = [
        49, 47, 46, 45, 32, 33, 31, 30, 34, 38,
        37, 36, 35, 1, 2, 8, 9, 10, 18, 19,
        21, 22, 28, 26, 27, 25, 23, 24, 20, 4,
        5, 3, 50, 6, 7, 11, 12, 13, 14, 15,
        16, 17, 29, 39, 40, 44, 43, 42, 41, 40
    ]
    longer_initial_list = [16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 15, 14, 13, 12, 11, 10, 6, 7, 8, 9]
    initial_list = [2, 3, 4, 5, 1]

    def test_NormalReverse(self):
        lst = deepcopy(self.initial_list)
        reverse(lst, 3)
        assert lst == [5, 4, 3, 2, 1]

    def test_LowerThanSize(self):
        lst = deepcopy(self.initial_list)
        reverse(lst, 1)
        assert lst == [3, 2, 4, 5, 1]

    def test_MaxIndex(self):
        lst = deepcopy(self.initial_list)
        assert max(lst, 0, 1) == 1

    def test_MinIndex(self):
        lst = deepcopy(self.initial_list)
        reverse(lst, 1)
        assert max(lst, 0, 1) == 0

    def test_EmptyList(self):
        lst = []
        reverse_sort(lst)
        assert lst == []

    def test_OneItemList(self):
        lst = [1]
        reverse_sort(lst)
        assert lst == [1]

    def test_BasicTest(self):
        lst = deepcopy(self.initial_list)
        reverse_sort(lst)
        assert is_reverse_sorted(lst)

    def test_LongListTest(self):
        lst = deepcopy(self.longer_initial_list)
        reverse_sort(lst)
        assert is_reverse_sorted(lst)

    def test_LongLongListTest(self):
        lst = deepcopy(self.long_long_initial_list)
        reverse_sort(lst)
        assert is_reverse_sorted(lst)
