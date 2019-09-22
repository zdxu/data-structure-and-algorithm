# -*- coding=utf-8 -*-


def selection_sort_method(arr: list):
    if not arr:
        return arr

    for i in range(len(arr)):
        min = arr[i]
        for j in range(i, len(arr)):
            if min > arr[j]:
                temp = min
                min = arr[j]
                arr[j] = temp
        arr[i] = min
    return arr


if __name__ == "__main__":
    arr = [1, 4, 10, 6, 7, 5, 4, 3, 2, 11, 15, 19, 13]
    print(selection_sort_method(arr))
