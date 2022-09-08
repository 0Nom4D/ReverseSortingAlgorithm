#!/usr/bin/env python3


def reverse(lst: list, idx: int) -> None:
    for i in range(idx):
        if i > idx:
            print(f'List after Reverse: {lst}')
            return
        lst[idx], lst[i] = lst[i], lst[idx]
        idx -= 1
    print(f'List after Reverse: {lst}')


def max(lst: list, idx1: int, idx2: int) -> int:
    return idx1 if lst[idx1] > lst[idx2] else idx2


def reverse_sort(lst: list) -> None:
    for i in range(len(lst) - 1, 0, -1):
        min_value = i
        for j in range(0, i):
            if max(lst, j, min_value) == min_value:
                min_value = j
        if i == min_value:
            continue
        print(i, min_value)
        reverse(lst, min_value)
        reverse(lst, i)
    print(f'Sorted List: {lst}')


def main() -> int:
    nb_list = [5, 4, 2, 1, 3]
    reverse_sort(nb_list)


if __name__ == "__main__":
    exit(main())
