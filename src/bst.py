# -*- coding: utf-8 -*-
class Node(object):
    """Building our Node class."""

    def __init__(self, val, left=None, right=None):
        """Class implements a node."""
        self.val = val
        self.left = left
        self.right = right


class BST(object):
    """Class implements a binary search tree data structure in Python."""

    def __init__(self, iterable=None):
        """Init method of bst class."""
        self.length = 0
        if iterable is None:
            self.root = None
            return
        for value in iterable:
            self.insert(value)

    def insert(self, val, node=None):
        new_node = Node(val)
        if node is None:
            node = self.root
        if not node:
            self.root = new_node
            self.length += 1
            return
        if val > node.val:
            if not node.right:
                node.right = new_node
                self.length += 1
            else:
                self.insert(val, node.right)
        elif val < node.val:
            if not node.left:
                node.left = new_node
                self.length += 1
            else:
                self.insert(val, node.left)

    def contains(self, val):
        current_node = self.root
        if current_node is None:
            return False
        if val == current_node.val:
            return True
        while True:
            if val > current_node.val and current_node.right is not None:
                current_node = current_node.right
                if current_node.val == val:
                    return True
            elif val < current_node.val and current_node.left is not None:
                current_node = current_node.left
                if current_node.val == val:
                    return True
            else:
                return False

    def size(self):
        return self.length

    def depth(self):
        pass

    def balance(self):
        pass
