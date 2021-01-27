""" Programma queue.py implements a queue

door Miro Zwering met ID 12910260
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

class Queue:
    def __init__(self):
        self._data = []

    # add element to back of queue (at the right of the list)
    def enqueue(self, element):
        self._data.append(element)

    # remove and return element from front of queue (at the left of the list)
    def dequeue(self):
        assert self.size() > 0
        return self._data.pop(0)

    def dequeue_var(self):
        if self._data:
            return self._data.pop(0)
        return None

    # return the number of elements waiting in the queue
    def size(self):
        return len(self._data)

    # return the frontmost (left) element but does not remove it from the queue yet
    def peek(self):
        if self._data:
            return self._data[0]
        return None

    # empty list
    def empty(self):
        self._data = []

    # empty list var
    def empty_var(self):
        self._data.clear()

    def is_empty(self):
        return not self._data

    def description(self):
        if self._data:
            return f"lengte is {len(self._data)}"
        return f"The list is empty"

    def __str__(self):
        return f"{self._data}"

