# -*- coding: utf-8 -*-
"""File implements a basic queue data structure."""
from __future__ import unicode_literals
import dll


class Queue(object):
    """Queue class implements a simple queue data structure."""

    def __init__(self, iterable=None):
        """Init queue, iterate through data if provided as an argument."""
        self.dll = dll.DoublyLinkedList(iterable)

    def enqueue(self, data):
        """Add a value to the head of the queue."""
        return self.dll.push(data)

    def dequeue(self):
        """Remove a value from the tail of the queue."""
        try:
            return self.dll.shift()
        except AttributeError:
            raise IndexError("This queue is empty.")

    def peek(self):
        """Return value of tail's previous node w/o removing it."""
        if self.dll.tail is None:
            return None
        return self.dll.tail.data

    def size(self):
        """Return size of the queue, 0 if empty."""
        count = 0
        current = self.dll.head
        while current is not None:
            count += 1
            current = current._next
        return count
