#!/usr/bin/env python3
"""
`stack` implementation

@authors: Roman Yasinovskyy
@version: 2021.11
"""

from queue import SimpleQueue
from typing import Any


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class Stack:
    """
    LIFO data structure

    Items are added and removed on the same end of the collection
    """

    def __init__(self):
        """Initialize a stack using queue.SimpleQueue"""
        # NOTE: DO not modify this method
        self.items = SimpleQueue()

    def push(self, item: Any) -> None:
        """
        Add a new item to stack

        :param item: a new item to push onto the stack
        """
        # TODO: Implement this method
        self.items.put(item)
        ...

    def pop(self) -> Any:
        """
        Remove an item from the stack

        :return: the top element of the stack
        :raise StackError is the stack is empty
        """
        # TODO: Implement this method
        if self.items.qsize() == 0:
            raise StackError('Cannot pop from an empty stack')
        pop_queue = SimpleQueue()
        if self.items.qsize() == 1:
            return self.items.get()
        while self.items.qsize() != 1:
            pop_queue.put(self.items.get())
        while pop_queue.qsize() != 0:
            self.items.put(pop_queue.get())
        return self.items.get()
        ...

    def peek(self) -> Any:
        """
        Look at the top item without removing it

        :return: the top element of the stack
        :raise StackError is the stack is empty
        """
        # TODO: Implement this method
        peek_queue = SimpleQueue()
        if self.items.qsize() == 0:
            raise StackError('Nothing to see here, the stack is empty')
        while self.items.qsize() != 1:
            peek_queue.put(self.items.get())
        top_item = self.items.get()
        peek_queue.put(top_item)
        while not peek_queue.empty():
            self.items.put(peek_queue.get())
        return top_item
        ...

    def __bool__(self) -> bool:
        """
        Evaluate the stack

        :return: False if the stack is empty, True otherwise
        """
        # TODO: Implement this method
        return not self.items.empty()
        ...

    def __len__(self) -> int:
        """
        Return the number of items in the stack

        :return: number of items in the stack (0 if the stack is empty)
        """
        # TODO: Implement this method
        return self.items.qsize()
        ...
