# -*- coding=utf-8 -*-
import sys
import os
from werkzeug import import_string


sys.path.append(os.getcwd().replace("sort_algorithm", ""))
insert_sort_method = \
    import_string("sort_algorithm.insertion_sort.insert_sort_method")


def shell_sort_method(arr: list, step):
    if step == 1:
        return insert_sort_method(arr)

    for i in range(step):
        j = i + step
        temp = arr[j]
        while j < len(arr):
            k = j - step
            while k > 0:
                if arr[k] > arr[j]:
                    temp = arr[j]
                    arr[j] = arr[k]
                    arr[k] = temp
                    k = k - step
                else:
                    break
            j = j + step
    return shell_sort_method(arr, step//2)


if __name__ == "__main__":
    arr = [1, 4, 10, 6, 7, 5, 4, 3, 2, 11, 15, 19, 13]
    print(shell_sort_method(arr, len(arr)//2))
