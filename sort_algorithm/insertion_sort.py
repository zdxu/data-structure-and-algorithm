# -*- coding=utf-8 -*-


def insert_sort_method(arr: list):
    if not arr:
        return arr

    for i in range(len(arr)):
        if 0 == i:
            continue

        temp = arr[i]
        for j in range(i):
            if arr[i - j] > temp:
                arr[i - j + 1] = arr[i - j]
                arr[i - j] = temp
    return arr


if __name__ == "__main__":
    arr = [1, 4, 10, 6, 7, 5, 4, 3, 2, 11, 15, 19, 13]
    print(insert_sort_method(arr))
