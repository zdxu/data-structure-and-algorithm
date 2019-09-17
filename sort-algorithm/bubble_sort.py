# -*- coding=utf-8 -*-


def bubble_sort_method(arr: list):
    if not arr:
        return arr

    for i in range(len(arr)):
        for j in range(len(arr) - i):
            if j > 0 and arr[j - 1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
    return arr


if __name__ == "__main__":
    arr = [1, 4, 10, 6, 7, 5, 4, 3, 2, 11, 15, 19, 13]
    print(bubble_sort_method(arr))
