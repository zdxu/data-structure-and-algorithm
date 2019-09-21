# -*- coding=utf-8 -*-
import math


class MaxHeap:

    def __init__(self, arr=[]):
        self._data = [None]
        for val in arr:
            self.push(val)

    def _val_to_top(self, idx):
        h = int(math.floor(math.log(idx + 1, 2)))
        if h == 1:
            p_idx = 0
        else:
            p_idx = int(math.pow(2, h - 1) + (idx - math.pow(2, h))//2)
        if p_idx != 0 and self._data[idx] > self._data[p_idx]:
            temp = self._data[idx]
            self._data[idx] = self._data[p_idx]
            self._data[p_idx] = temp
            self._val_to_top(p_idx)
        return

    def _val_to_bottom(self, idx):
        if idx >= len(self._data):
            return

        h = int(math.floor(math.log(idx + 1, 2)))
        lni = int(math.pow(2, h + 1) + (idx - math.pow(2, h))*2)
        rni = lni + 1
        if lni >= len(self._data):
            return
        elif rni >= len(self._data):
            cidx = lni
        else:
            cidx = self._max_val_idx(lni, rni)
        if self._data[idx] < self._data[cidx]:
            temp = self._data[idx]
            self._data[idx] = self._data[cidx]
            self._data[cidx] = temp
            self._val_to_bottom(cidx)

    def _max_val_idx(self, lni, rni):
        if self._data[lni] >= self._data[rni]:
            return lni
        else:
            return rni

    def push(self, val):
        self._data.append(val)
        idx = len(self._data) - 1
        self._val_to_top(idx)

    def pop(self):
        self_len = len(self._data)
        if self_len == 1:
            raise ValueError("heap is empty.")
        elif self_len == 2:
            val = self._data[1]
            del self._data[1]
            return val
        else:
            idx = self._max_val_idx(1, 2)
            val = self._data[idx]
            self._data[idx] = self._data[self_len - 1]
            del self._data[self_len - 1]
            self._val_to_bottom(idx)
            return val

    @property
    def length(self):
        return len(self._data) - 1


if __name__ == "__main__":
    heap = MaxHeap([1, 8, 9, 10, 22, 45, 2, 4, 5, 11, 14, 27, 32])
    print(heap.pop())
    print(heap.push(100))
    print(heap.pop())

    heap_len = heap.length
    for i in range(heap_len):
        print(heap.pop())
