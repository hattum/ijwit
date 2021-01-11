""" Programma queue.py implements a queue

door Miro Zwering met ID 12910260
"""
import itertools
from collections import OrderedDict

offsets = OrderedDict()
offsets = {
    "1": [0, 1],
    "-1": [0, -1],
    "2": [-1, 0],
    "-2": [1, 0]
}

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

    # def fill_que(self, string):
    #     for ch in string:
    #         self.enqueue(ch)

class AminoQueue(Queue):
    def __init__(self, string):
        super().__init__()
        self.string = string
        return self.fill(string)

    def fill(self, string):
        for ch in string:
            self.enqueue(ch)

    def cyclefold(self):
        directs = ["2", "1", "-2", "-1"]
        directions_cycle = itertools.cycle(directs)
        start_amino = self.dequeue()
        current_pos = (int(len(self.string)/2) - 1,int(len(self.string)/2) - 1)
        print("Current-ami is:",start_amino)
        print("Current-pos is:",current_pos)
        amino_path = [current_pos]
        predecessors= {current_pos: None}
        directions = {}
        directions2 = []

        while not self.is_empty():
            direction = next(directions_cycle)
            print("DIRECTION:",direction)
            next_amino = self.dequeue()
            print("Next-ami is:",next_amino)
            neighbour = (current_pos[0] + offsets[direction][0], 
                        current_pos[1] + offsets[direction][1])
            print("Pos:", neighbour)
            if neighbour not in directions:
                print("STARTER:", start_amino)
                directions2.append((start_amino, direction))
                directions[current_pos] = direction
                predecessors[neighbour] = current_pos
                start_amino = next_amino
                current_pos = neighbour
                print("PosValid is:",current_pos)
                amino_path.append(current_pos)
                
            
            elif neighbour in directions:
                while neighbour in directions:
                    direction = next(directions_cycle)
                    direction = next(directions_cycle)
                    direction = next(directions_cycle)
                    directions[current_pos] = direction
                    print("OnGoing-ami is:", next_amino)
                    print("OnGoing-pos is:",current_pos)
                    print("DIRECTION:",direction)
                    neighbour = (current_pos[0] + offsets[direction][0], 
                                current_pos[1] + offsets[direction][1])
                    print("OnGoing-ami is:", next_amino)
                    print("Neighbour is:", neighbour)
                predecessors[neighbour] = current_pos
                directions2.append((start_amino, direction))
                directions[neighbour] = direction
                start_amino = next_amino
                current_pos = neighbour
                print("Current-pos is:",current_pos)
                amino_path.append(current_pos)
        directions2.append((next_amino,self.size()))
        return amino_path, predecessors, directions, directions2

# def main():
#     q = Queue()          # create new queue
#     q.enqueue(3)         # add number 3 to back of queue
#     q.enqueue(2)         # add number 2 to back of queue
#     q.enqueue(1)         # add number 1 to back of queue
#     print(q.dequeue())   # prints first number "in", so 3
#     print(q.peek())
#     q.empty_var()
#     print(q.size())
#     print(q.description())
#     print(q)


# if __name__ == "__main__":
#     main()