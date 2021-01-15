import copy
from helpers_miro import offsets
from queue_miro import Queue, AminoQueue
from priorityqueue_miro import PriorityQueue


def priority_miro(start, depth):

    string = "ABCDEFGH" #mee bezig: fase implementatie karakters
    amino_q = AminoQueue(string) #mee bezig: fase implementatie karakters
    start_amino = amino_q.dequeue() #mee bezig: fase implementatie karakters
    pq = PriorityQueue()
    direction = "2"
    starter_amino = amino_q.dequeue() #mee bezig: fase implementatie karakters
    neighbour_pos = (start[0] + offsets[direction][0], 
                    start[1] + offsets[direction][1])
    score = 0
    pq.put([start,neighbour_pos], score)
    paths = []
    predecessors = {start: None, neighbour_pos: start}
    directions = {start: direction} #mee bezig: fase implementatie karakters
    print("Directions is:", directions)
    directions2 = [(start_amino, direction)] #mee bezig: fase implementatie karakters
    print("Directions2 is:", directions2)

    while not pq.is_empty():
        state = pq.get()
        print("State is:", state)
        if len(state) < depth:
            if len(state) == 2:
                for direction in ["2", "1"]:
                    neighbour_pos = (state[-1][0] + offsets[direction][0], 
                        state[-1][1] + offsets[direction][1])
                    child = copy.deepcopy(state)
                    if neighbour_pos not in child and child not in paths:
                        child += [neighbour_pos]
                        score = 0
                        pq.put(child, score)
                        predecessors[neighbour_pos] = state[-1]
                        if len(child) == depth:
                            paths.append(child)
            elif len(state) != 2:
                for direction in ["2", "1", "-2", "-1"]:
                    neighbour_pos = (state[-1][0] + offsets[direction][0], 
                        state[-1][1] + offsets[direction][1])
                    child = copy.deepcopy(state)
                    if neighbour_pos not in child and child not in paths:
                        child += [neighbour_pos]
                        score = 0
                        pq.put(child, score)
                        predecessors[neighbour_pos] = state[-1]
                        if len(child) == depth:
                            paths.append(child)

    print(f"\nPaths with depth{depth} are:", paths)
    print("\nLengthPaths is:", len(paths))

def main():

    start = (0,0)
    print(priority_miro(start, 5))

if __name__ == "__main__":
    main()
    