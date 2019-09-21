# -*- coding=utf-8 -*-


from tree.heap import MaxHeap


def heap_sort_method(arr: list):
    heap = MaxHeap(arr)
    heap_len = heap.length
    data = []
    for i in heap_len:
        data.append(heap.pop())
    return data


if __name__ == "__main__":
    arr = [1, 4, 10, 6, 7, 5, 4, 3, 2, 11, 15, 19, 13]
    print(heap_sort_method(arr))
