# -*- coding=utf-8 -*-
import math


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class MaxHeap:

    root = Node(1000, 2)

    def __init__(self):
        self.arr = [self.root]

    @staticmethod
    def tree_height(tree_element_count):
        return math.floor(math.log(tree_element_count, 2))

    @staticmethod
    def parent_node_idx(cur_node_idx):
        if cur_node_idx < 2:
            raise Exception("Parent node is not exist.")

        tree_element_count = cur_node_idx
        h = MaxHeap.tree_height(tree_element_count)
        # math.pow(2, h - 1)  父节点所在层的第一个节点的索引
        # cur_node_idx - math.pow(2, h)  当前节点与父节点所在层的第一个节点的索引
        # math.ceil.((cur_node_idx - math.pow(2, h)) // 2)  当前节点与当前节点所在层
        # 的第一个节点的索引的差值
        return int(math.pow(2, h - 1)) + (cur_node_idx - int(math.pow(2, h))) // 2

    def max_sub_node_idx(self, cur_idx):
        h = MaxHeap.tree_height(cur_idx)
        left_sub_node_idx = int(math.pow(2, h + 1)) + (cur_idx - int(math.pow(2, h))) * 2
        right_sub_node_idx = left_sub_node_idx + 1
        if right_sub_node_idx > self.length - 1:
            if left_sub_node_idx > self.length - 1:
                return None
            else:
                return left_sub_node_idx

        if self.arr[left_sub_node_idx].key >= self.arr[right_sub_node_idx].key:
            return left_sub_node_idx
        else:
            return right_sub_node_idx

    def __to_top(self, cur_idx=0):
        if 0 == cur_idx:
            cur_idx = self.length

        # 当前节点已是根节点
        if 1 == cur_idx:
            return

        parent_node_idx = MaxHeap.parent_node_idx(cur_idx)
        # 父节点小于当前节点则进行节点交换
        if self.arr[cur_idx].key > self.arr[parent_node_idx].key:
            temp = self.arr[cur_idx]
            self.arr[cur_idx] = self.arr[parent_node_idx]
            self.arr[parent_node_idx] = temp
            self.__to_top(parent_node_idx)

    def __to_bottom(self, cur_idx=0):
        if 1 == self.length:
            return

        if 0 == cur_idx:
            cur_idx = 1

        sub_node_idx = self.max_sub_node_idx(cur_idx)
        if sub_node_idx is None:
            return

        if self.arr[cur_idx].key < self.arr[sub_node_idx].key:
            temp = self.arr[cur_idx]
            self.arr[cur_idx] = self.arr[sub_node_idx]
            self.arr[sub_node_idx] = temp
            cur_idx = sub_node_idx
            self.__to_bottom(cur_idx)

    def push(self, node):
        self.arr.append(node)
        self.__to_top()

    def pop(self):
        if 0 == self.length:
            raise Exception("Current heap is empty.")
        pop_node = self.arr[1]
        self.arr[1] = self.arr[self.length]
        del self.arr[self.length]
        self.__to_bottom()
        return pop_node

    @property
    def length(self):
        return len(self.arr) - 1

if __name__ == "__main__":
    heap = MaxHeap()
    heap.push(Node(1, 2))
    heap.push(Node(2, 2))
    heap.push(Node(8, 2))
    heap.push(Node(4, 2))
    heap.push(Node(5, 2))
    heap.push(Node(12, 2))
    heap.push(Node(15, 2))
    heap.push(Node(7, 2))
    heap.push(Node(102, 2))

    print(heap.pop().key)
    print(heap.pop().key)

    heap_len = heap.length
    for i in range(heap_len):
        print(heap.pop().key)

