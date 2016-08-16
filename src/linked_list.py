# -*- coding: utf-8 -*-
"""This file implements a basic linked list data structure."""
import sys


class Node(object):
    """This builds our Node class."""

    def __init__(self, data):
        """Initial setup of Node objects."""
        self.data = data
        self.next_node = None


class LinkedList(object):
    """This builds LinkedList class."""

    def __init__(self, data):
        """Initial setup of LinkedList class."""
        self.head = None
        try:
            if data:
                for item in data:
                    self.push(item)
        except TypeError:
            print('Please enter an iterable object.')

    def push(self, data):
        """Function builds push method of LinkedList class."""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        return self.head

    def pop(self):
        """Function builds pop method of LinkedList class."""
        pop_node = self.head
        self.head = self.head.next_node
        return pop_node

    # def size():

    # def search(data)
    #
    # def remove(node)
    #
    # def display():

# if __name__ == '__main__':
#     LinkedList(sys.argv[1])
