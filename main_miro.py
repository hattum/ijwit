from helpers_miro import offsets
from queue_miro import Queue
import itertools

def main():

    directions = ["up", "right", "down", "left"]

    directions_cycle = itertools.cycle(directions)

    amino_poss = []

    neighbours = {}

    amino_q = Queue()

    amino_string = "HHPHHHPH"

    graph = [["  " for i in range(len(amino_string))] for i in range(len(amino_string))]

    for ch in amino_string:
        amino_q.enqueue(ch)

    current_pos = (3,3)

    amino_poss.append(current_pos)
    current_amino = amino_q.dequeue()

    neighbours[current_pos] = None
    
    while not amino_q.is_empty():
        current_amino = amino_q.dequeue()
        direction = next(directions_cycle)
        neighbour = (current_pos[0] + offsets[direction][0], 
                    current_pos[1] + offsets[direction][1])
        if neighbour not in neighbours:
            neighbours[neighbour] = current_pos
            current_pos = neighbour
            amino_poss.append(current_pos)
        
        elif neighbour in neighbours:
            while neighbour in neighbours:
                direction = next(directions_cycle)
                neighbour = (current_pos[0] + offsets[direction][0], 
                            current_pos[1] + offsets[direction][1])
        
            neighbours[neighbour] = current_pos
            current_pos = neighbour
            amino_poss.append(current_pos)
            #print("Hoi")

    print("\nAmino_posities:")
    print(amino_poss)
    print()
    print("Current: Voorganger")

    for nb in neighbours:
        print(nb, ":" , neighbours[nb])
            
    for j, element in enumerate(zip(amino_poss, list(amino_string))):
        i = element[0]
        graph[i[0]][i[1]] = element[1]+str(j)
        
    print()
    print("Representatie:")

    for row in graph:
         print(row)

if __name__ == "__main__":
    main()