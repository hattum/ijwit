""" Programma queue.py implements a queue

door Miro Zwering met ID 12910260
"""
import itertools
from collections import OrderedDict
from copy import deepcopy

offsets = OrderedDict()
offsets = {
    "1": [0, 1],
    "-1": [0, -1],
    "2": [-1, 0],
    "-2": [1, 0]
}

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
        amino_paths = []
        predecessors= {current_pos: None}
        directions = {}
        directions2 = []

        direction = next(directions_cycle)
        starter_amino = self.dequeue()
        currenter_pos = (current_pos[0] + offsets[direction][0], 
                    current_pos[1] + offsets[direction][1])
        amino_path += [currenter_pos]
        predecessors[currenter_pos] = current_pos
        directions[current_pos] = direction
        directions2.append((start_amino, direction))

        while not self.is_empty():
            direction = next(directions_cycle)
            print("DIRECTION:",direction)
            next_amino = self.dequeue()
            print("Next-ami is:",next_amino)
            neighbour = (currenter_pos[0] + offsets[direction][0], 
                        currenter_pos[1] + offsets[direction][1])
            print("Pos:", neighbour)
            if neighbour not in directions:
                print("STARTER:", start_amino)
                directions2.append((starter_amino, direction))
                directions[currenter_pos] = direction
                predecessors[neighbour] = currenter_pos
                starter_amino = next_amino
                currenter_pos = neighbour
                print("PosValid is:",currenter_pos)
                amino_path.append(currenter_pos)
                

            elif neighbour in directions:
                while neighbour in directions:
                    direction = next(directions_cycle)
                    direction = next(directions_cycle)
                    direction = next(directions_cycle)
                    directions[currenter_pos] = direction
                    print("OnGoing-ami is:", next_amino)
                    print("OnGoing-pos is:",current_pos)
                    print("DIRECTION:",direction)
                    neighbour = (currenter_pos[0] + offsets[direction][0], 
                                currenter_pos[1] + offsets[direction][1])
                    print("OnGoing-ami is:", next_amino)
                    print("Neighbour is:", neighbour)
                predecessors[neighbour] = currenter_pos
                directions2.append((starter_amino, direction))
                directions[neighbour] = direction
                starter_amino = next_amino
                currenter_pos = neighbour
                print("Current-pos is:",currenter_pos)
                amino_path.append(currenter_pos)
        last_amino = directions2.pop()
        laster_amino = last_amino[0]
        print("Last amino is:", last_amino)
        laster_amino = last_amino[0]
        print("Laster amino is:", laster_amino)
        directions2.append((laster_amino, self.size()))
        #directions2.append((next_amino,self.size()))
        #directions2[-1]= (start_amino, self.size())
        #directions2[-1]= ("GEK",self.size())
        #directions2[-1][1]= str(self.size())
        return amino_path, predecessors, directions, directions2

    
    def cyclefold2(self):
        directs = ["2", "1", "-2", "-1"]
        directions_cycle = itertools.cycle(directs)
        start_amino = self.dequeue()
        current_pos = (int(len(self.string)/2) - 1,int(len(self.string)/2) - 1)
        print("Current-ami is:",start_amino)
        print("Current-pos is:",current_pos)
        amino_path = [current_pos]
        amino_paths = []
        predecessors= {current_pos: None}
        directions = {}
        directions2 = []

        direction = "2"
        starter_amino = self.dequeue()
        currenter_pos = (current_pos[0] + offsets[direction][0], 
                    current_pos[1] + offsets[direction][1])
        amino_path += [currenter_pos]
        predecessors[currenter_pos] = current_pos
        directions[current_pos] = direction
        directions2.append((start_amino, direction))

        while not self.is_empty():
            next_amino = self.dequeue()
            #counter = 0
            for i in range(len(directs) - 1):
                direction = next(directions_cycle)
                #counter = counter + 1
                print("Currenter_pos is:", currenter_pos)
                neighbour_pos = (currenter_pos[0] + offsets[direction][0], 
                            currenter_pos[1] + offsets[direction][1])
                print("NeighbourPos is:", neighbour_pos)
                if neighbour_pos not in directions:
                    #directions[currenter_pos] = direction
                    print("Directions is:", directions)
                    directions2.append((starter_amino, direction))
                    predecessors[neighbour_pos] = currenter_pos
                    starter_amino = next_amino
                    currenter_pos = neighbour_pos
                    child = deepcopy(amino_path)
                    child.append(neighbour_pos)
                #amino_paths.append(child)
                    
                elif neighbour_pos in directions:
                    #while neighbour_pos in directions:
                    direction = next(directions_cycle)
                    #direction = next(directions_cycle)
                    #direction = next(directions_cycle)
                    #direction = next(directions_cycle)
                    directions[currenter_pos] = direction
                    print("OnGoing-ami is:", next_amino)
                    print("OnGoing-pos is:",currenter_pos)
                    print("DIRECTION:",direction)
                    neighbour_pos = (currenter_pos[0] + offsets[direction][0], 
                                currenter_pos[1] + offsets[direction][1])
                    print("OnGoing-ami is:", next_amino)
                    print("Neighbour is:", neighbour_pos)
                    predecessors[neighbour_pos] = currenter_pos
                    directions2.append((starter_amino, direction))
                    directions[neighbour_pos] = direction
                    starter_amino = next_amino
                    #currenter_pos = neighbour
                    print("NEIGHBOUR is:", neighbour_pos)
                    #child.append(neighbour)
                    print("Current-pos is:",current_pos)
                amino_paths.append(child)
            last_amino = directions2.pop()
            laster_amino = last_amino[0]
            directions2.append((laster_amino, self.size()))
            print("Aminopaths is:", amino_paths)
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