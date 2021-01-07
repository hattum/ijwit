""" Programma queue.py implements a queue

door Miro Zwering met ID 12910260
"""


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
        #return len(self._data) == 0
        #return self._data == []
        return not self._data

    def description(self):
        if self._data:
            return f"lengte is {len(self._data)}"
        return f"The list is empty"

    def __str__(self):
        return f"{self._data}"

def main():
    q = Queue()          # create new queue
    q.enqueue(3)         # add number 3 to back of queue
    q.enqueue(2)         # add number 2 to back of queue
    q.enqueue(1)         # add number 1 to back of queue
    print(q.dequeue())   # prints first number "in", so 3
    print(q.peek())
    q.empty_var()
    print(q.size())
    print(q.description())
    print(q)


if __name__ == "__main__":
    main()