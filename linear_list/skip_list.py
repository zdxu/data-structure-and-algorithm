# -*- coding: utf-8 -*-


# !/usr/bin/python
import random
import math


class Node:

    def __init__(self, key, val):
        self.nodes = {}
        self.key = key
        self.val = val

    def next_set(self, level, next_node):
        self.nodes[level] = next_node

    def next_get(self, level):
        return self.nodes.get(level, None)

    def next_del(self, level):
        if not self.next_get(level):
            raise ValueError("Node is not exist.")
        del self.nodes[level]

    def level_get(self):
        return len(self.nodes)

    def update(self, key, val):
        self.key = key
        self.val = val


class SkitList:
    max_level = 32

    def __init__(self):
        self.head = None
        self.level = 1

    def search(self, key):
        # 空表
        if not self.head:
            return None

        ret = None
        pre_node = self.head
        cur_level = self.level
        # 层级遍历
        while cur_level > 0:
            cur_node = pre_node
            # 遍历当前层级节点，获取最靠近插入元素的左元素
            while cur_node and key >= cur_node.key:
                pre_node = cur_node
                cur_node = cur_node.next_get(cur_level)

            # 获取到元素中断遍历
            if key == pre_node.key:
                ret = pre_node
                break
            cur_level -= 1

        return ret

    def add(self, key, val):
        new_node = Node(key, val)

        # 空表添加
        if not self.head:
            self.head = new_node
            return

        # 元素已被添加，更新值
        cur_node = self.search(key)
        if cur_node:
            cur_node.update(key, val)
            return

        # 获取随机层级
        level = self.random_level()

        # 表前插入，调换头元素与插入元素属性，并将入调换后插入元素的层级设为当前跳跃表层级
        if key < self.head.key:
            new_node = Node(self.head.key, self.head.val)
            self.head.update(key, val)
            level = self.level

        pre_node = self.head
        cur_level = level
        # 插入元素层级高于头元素的层级
        if self.level < cur_level:
            while self.level < cur_level:
                self.head.next_set(cur_level, new_node)
                cur_level -= 1
            self.level = level

        while cur_level > 0:
            cur_node = pre_node
            # 获取当前层级插入元素的前一元素
            while cur_node and new_node.key > cur_node.key:
                pre_node = cur_node
                cur_node = cur_node.next_get(cur_level)

            pre_node.next_set(cur_level, new_node)
            # 元素插在两个层级元素之间
            if cur_node:
                new_node.next_set(cur_level, cur_node)

            cur_level -= 1

        return new_node

    def delete(self, key):
        if not self.head:
            raise Exception("Node is not exist.")

        del_node = self.search(key)
        if not del_node:
            raise Exception("Node is not exist.")

        # 删跳跃表头元素
        if self.head == del_node:
            if not self.head.next_get(1):
                self.head = None
            else:
                temp = self.head
                self.head = temp.next_get(1)
                for i in range(self.level):
                    cur_level = self.level - i
                    cur_node = temp.next_get(cur_level)
                    # 替换元素小于当前跳跃表层级的部分沿用原先的 next
                    if cur_node != self.head:
                        self.head.next_set(cur_level, cur_node)
                    else:
                        break
        else:
            cur_level = self.level
            pre_node = self.head
            while cur_level > 0:
                cur_node = pre_node
                # 当前层级最接近删除元素的左侧元素
                while cur_node and cur_node.key < del_node.key:
                    pre_node = cur_node
                    cur_node = cur_node.next_get(cur_level)

                if cur_node == del_node:
                    # 删除被删除元素当前层级
                    if cur_node.next_get(cur_level):
                        pre_node.next_set(cur_level, cur_node.next_get(cur_level))
                    else:
                        pre_node.next_del(cur_level)

                cur_level -= 1

    def random_level(self):
        int_random_val = random.randint(1, math.pow(2, self.max_level))
        level = self.max_level - math.floor(math.log(int_random_val, 2))
        return level


if __name__ == '__main__':
    skit_list = SkitList()
    skit_list.add(2, 3)
    skit_list.add(3, 3)
    skit_list.add(5, 3)
    skit_list.add(1, 3)
    skit_list.add(8, 3)
    skit_list.add(2, 5)
    skit_list.add(4, 3)
    skit_list.add(6, 3)
    skit_list.add(10, 3)
    skit_list.add(15, 3)
    skit_list.add(12, 3)
    skit_list.add(24, 3)
    skit_list.add(20, 3)

    node = skit_list.search(10)
    print(node)

    skit_list.delete(1)

    skit_list.delete(24)

    print(skit_list)
