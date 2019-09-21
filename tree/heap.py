# -*- coding=utf-8 -*-
import math


class MaxHeap:

    def __init__(self, arr=[]):
        self._data = [None]  # 根节点不存放具体值，方便操作，也可放限值
        for val in arr:
            self.push(val)

    def _val_to_top(self, idx):
        # 当前 idx 所处树高
        h = int(math.floor(math.log(idx + 1, 2)))
        if h == 1:  # 树高为 1，则父节点索引为根节点即 0
            p_idx = 0
        else:
            # 父节点索引值
            # math.pow(2, h - 1) 父节点所在层的首个节点的索引
            # idx - math.pow(2, h) 当前节点与所在层首节点索引差值
            # (idx - math.pow(2, h))//2 父节点所在层的首个节点的索引与父节点索引的差值
            p_idx = int(math.pow(2, h - 1) + (idx - math.pow(2, h))//2)
        if p_idx != 0 and self._data[idx] > self._data[p_idx]:
            # 父节点非根节点且当前节点值大于父节点值，发生交换
            temp = self._data[idx]
            self._data[idx] = self._data[p_idx]
            self._data[p_idx] = temp
            self._val_to_top(p_idx)
        return

    def _val_to_bottom(self, idx):
        if idx >= len(self._data):
            return

        # 当前 idx 所处树高
        h = int(math.floor(math.log(idx + 1, 2)))
        # lni idx 节点的左子节点的索引
        # rni idx 节点的右子节点的索引
        lni = int(math.pow(2, h + 1) + (idx - math.pow(2, h))*2)
        rni = lni + 1
        if lni >= len(self._data):
            return
        # cidx idx 节点的子节点中值最大的节点的索引
        elif rni >= len(self._data):
            cidx = lni
        else:
            cidx = self._max_val_idx(lni, rni)
        if self._data[idx] < self._data[cidx]:
            # 父节点的值比子节点的值小，发生交换
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
        # 弹出头部最大值，并用数组最末元素替换
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
