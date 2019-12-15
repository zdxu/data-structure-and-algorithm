# -*- coding: utf-8 -*-


class Element:

    def __init__(self, val):
        self.val = val


class Node:

    def __init__(self, elements, parent=None, sub_nodes=None):
        self.elements = elements
        self.parent = parent
        self.sub_nodes = sub_nodes


class TTFTree:

    def __init__(self):
        self.root = None

    def search(self, val):
        node = self.root
        while node:
            flag, idx = TTFTree.compare_with_node_elements(node.elements, val)
            # 在比对节点的元素中匹配到等于 val 的元素
            if flag:
                return node, idx

            # 无子节点可查
            if not node.sub_nodes:
                return None, None

            # 可能存在的子节点
            node = node.sub_nodes[idx]

        return None, None

    @staticmethod
    def compare_with_node_elements(elements, val):
        """
        :param elements: 比对节点元素列表
        :param val:  比对值
        :return: flag， idx；flag True 匹配上 False 未匹配上，idx 节点元素下标 或 对应子节点下标
        """
        flag = False
        idx = 0
        for element in elements:
            if element.val > val:
                return flag, idx
            elif element.val == val:
                flag = True
                return flag, idx
            elif element.val < val:
                idx += 1
        return flag, idx

    def insert(self, val):
        if self.root is None:
            elements = [Element(val)]
            self.root = Node(elements=elements)
            return self.root

        # 元素将要插入的节点
        in_node = self.root
        while in_node.sub_nodes:
            flag, idx = TTFTree.compare_with_node_elements(in_node.elements, val)
            if flag:
                idx += 1
            in_node = in_node.sub_nodes[idx]

        element = Element(val)
        # 节点元素小于 3，直接插入
        if 3 > len(in_node.elements):
            TTFTree.node_element_add(in_node, element)
        else:
            # 节点中间元素提升至父节点，子节点分裂

            # 满叶子节点上移过程
            self.element_up_to_node(in_node, element, None, None)

    @staticmethod
    def node_element_add(node, element):
        # 元素将要插入的索引坐标
        flag, idx = TTFTree.compare_with_node_elements(node.elements, element.val)
        if flag:
            idx = idx + 1

        if 0 == idx:
            node.elements = [element] + node.elements
        elif len(node.elements) < idx:
            node.elements = node.elements + [element]
        else:
            node.elements = node.elements[0: idx] + [element] + \
                            node.elements[idx: len(node.elements)]
        return idx

    def element_up_to_node(self, node, upward_element, lnode, rnode):
        """
        :param node: 上移元素将要移入的节点
        :param upward_element: 上移元素
        :param lnode: 上移元素的左子叶
        :param rnode: 上移元素的右子叶
        :return:
        """
        if node is None or len(node.elements) < 3:
            # 上移元素做根节点
            if node is None:
                node = Node([upward_element])
                node.sub_nodes = [lnode, rnode]
                self.root = node
            else:
                # 上移原素添加至节点中
                idx = TTFTree.node_element_add(node, upward_element)
                del node.sub_nodes[idx]
                node.sub_nodes.insert(idx, rnode)
                node.sub_nodes.insert(idx, lnode)
            lnode.parent = node
            rnode.parent = node
        # 移入节点为满元素节点，合并元素后，节点分裂并将原中间元素上移
        else:
            idx = TTFTree.node_element_add(node, upward_element)
            # 移入节点为叶子节点
            if not node.sub_nodes or 0 == len(node.sub_nodes):
                # 剔出上移元素，分裂移入节点
                if 1 >= idx:
                    upward_element, lnode, rnode = node.elements[2], Node(node.elements[0:2]), \
                                                   Node(node.elements[3:4])
                else:
                    upward_element, lnode, rnode = node.elements[1], Node(node.elements[0:1]), \
                                                   Node(node.elements[2:4])
            else:
                # 移入节点非叶子节点，多了一步合并子节点的操作
                old_lnode = lnode
                old_rnode = rnode
                if 1 >= idx:
                    upward_element, lnode, rnode = node.elements[2], Node(node.elements[0:2]), \
                                                   Node(node.elements[3:4])
                    rnode.sub_nodes = node.sub_nodes[2:4]
                    if 0 == idx:
                        lnode.sub_nodes = [old_lnode, old_rnode] + node.sub_nodes[1:2]
                    else:
                        lnode.sub_nodes = node.sub_nodes[0:1] + [old_lnode, old_rnode]
                    old_lnode.parent = lnode
                    old_rnode.parent = lnode
                else:
                    upward_element, lnode, rnode = node.elements[1], Node(node.elements[0:1]), \
                                                   Node(node.elements[2:4])
                    lnode.sub_nodes = node.sub_nodes[0:2]
                    if 2 == idx:
                        rnode.sub_nodes = [old_lnode, old_rnode] + node.sub_nodes[3:4]
                    else:
                        rnode.sub_nodes = node.sub_nodes[2:3] + [old_lnode, old_rnode]
                    old_lnode.parent = rnode
                    old_rnode.parent = rnode
            self.element_up_to_node(node.parent, upward_element, lnode, rnode)

    def delete(self, val):
        node, idx = self.search(val)
        if not node:
            raise Exception("Node is not exist.")

        # 根节点，直接删除元素或者删除节点并将根节点置为 None
        if self.root == node and not node.sub_nodes:
            if 1 == len(node.elements):
                self.root = None
            else:
                del node.elements[idx]
            return

        # 用右子树的最左子叶的第一个元素替换删除的元素
        if not node.sub_nodes:
            leaf_node = node
        else:
            leaf_node = TTFTree.left_tree_min_node(node.sub_nodes[idx + 1])
            node.elements[idx] = leaf_node.elements[0]

        TTFTree.no_root_node_first_element_del(leaf_node)

    @staticmethod
    def left_tree_min_node(root):
        sub_node = root
        while not sub_node.sub_nodes:
            sub_node = sub_node.sub_nodes[0]
        return sub_node

    @staticmethod
    def no_root_node_first_element_del(node):
        parent = node.parent
        # 删除节点所在父类子节点的下标
        for idx in range(len(parent.sub_nodes)):
            if parent.sub_nodes[idx] == node:
                break

        # 左旋或合并节点
        if 0 == idx or 2 == idx:
            # 将要删除元素节点与其平级后一节点元素总和为 3，删除后元素将发生合并
            if (len(parent.sub_nodes[idx].elements) + len(parent.sub_nodes[idx + 1].elements)) == 3:
                elements = parent.sub_nodes[idx].elements + parent.elements + parent.sub_nodes[idx + 1].elements
                # 父节点只有一个元素，三个节点合并为新的父节点
                if 1 == len(parent.elements):
                    parent.elements = elements
                    parent.sub_nodes = None
                    del parent.elements[idx]
                # 父节点超过一个元素，三个节点合并为新的子节点
                else:
                    del parent.elements[idx]
                    del parent.sub_nodes[idx]
                    del parent.sub_nodes[idx + 1]
                    parent.sub_nodes.insert(0, Node(elements))
            # 将要删除元素节点与其平级后一节点元素总和为 4 且父节点为单元素，删除后元素将发生左旋
            elif (len(parent.sub_nodes[idx].elements) + len(parent.sub_nodes[idx + 1].elements)) == 4 or \
                    1 == len(node.elements):
                parent.sub_nodes[idx].elements[0] = parent.elements[idx]
                parent.elements[idx] = parent.sub_nodes[idx + 1].elements[0]
                del parent.sub_nodes[idx + 1].elements[0]
            else:
                del node.elements[0]
        # 右旋或合并节点（与左旋或合并类似）
        else:
            if (len(parent.sub_nodes[idx].elements) + len(parent.sub_nodes[idx + 1].elements)) == 3:
                elements = parent.sub_nodes[idx - 1].elements + parent.elements + parent.sub_nodes[idx].elements
                if 1 == len(parent.elements):
                    parent.elements = elements
                    parent.sub_nodes = None
                    del parent.elements[idx - 1]
                else:
                    del parent.elements[idx - 1]
                    del parent.sub_nodes[idx]
                    del parent.sub_nodes[idx - 1]
                    parent.sub_nodes.append(Node(elements))
            elif (len(parent.sub_nodes[idx - 1].elements) + len(parent.sub_nodes[idx].elements)) == 4 or \
                    1 == len(node.elements):
                parent.sub_nodes[idx].elements[0] = parent.elements[idx - 1]
                parent.elements[idx - 1] = parent.sub_nodes[idx - 1].elements[0]
                del parent.sub_nodes[idx - 1].elements[0]
            else:
                del node.elements[0]

    def print(self):
        pass


if __name__ == '__main__':
    tree = TTFTree()
    tree.insert(1)
    tree.insert(4)
    tree.insert(6)
    tree.insert(9)
    tree.insert(12)
    tree.insert(23)
    tree.insert(432)
    tree.insert(34)
    tree.insert(53)
    tree.insert(26)
    node, idx = tree.search(26)
    if node:
        print(node.elements[idx].val)

    tree.delete(26)
    node, idx = tree.search(26)
    if node:
        print(node.elements[idx].val)

