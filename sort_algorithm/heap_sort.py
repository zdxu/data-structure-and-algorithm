# -*- coding=utf-8 -*-
import sys
import os
from werkzeug import import_string


sys.path.append(os.getcwd().replace("sort-algorithm", ""))
MaxHeap = import_string("tree.heap.MaxHeap")


def heap_sort_method(arr: list):
    heap = MaxHeap(arr)
    heap_len = heap.length
    data = []
    for i in range(heap_len):
        data.append(heap.pop())
    return data


if __name__ == "__main__":
    arr = [1, 4, 10, 6, 7, 5, 4, 3, 2, 11, 15, 19, 13]
    print(heap_sort_method(arr))
