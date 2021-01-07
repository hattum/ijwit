from helpers_miro import offsets
from queue_miro import Queue
#import random
import itertools

def main():

    directions = ["up", "right", "down", "left"]

    directions_cycle = itertools.cycle(directions)

    amino_poss = []

    neighbours = {}

    amino_q = Queue()

    amino_string = "HHPHHHPH"

    for ch in amino_string:
        amino_q.enqueue(ch)

    current_pos = (0,0)

    amino_poss.append(current_pos)

    neighbours[current_pos] = None
    
    while not amino_q.is_empty():

        current_amino = amino_q.dequeue()
        #print(current_amino, "-", end = "")
        direction = next(directions_cycle)
        neighbour = (current_pos[0] + offsets[direction][0], 
                    current_pos[1] + offsets[direction][1])
        if neighbour not in neighbours:
            neighbours[neighbour] = current_pos
            current_pos = neighbour
            amino_poss.append(current_pos)
            print("\n New_Pos is: ", current_pos)
        
        #if neighbour in neighbours:
            #direction = next(directions_cycle)

    print("\n Amino_posities")
    print(amino_poss)
    print()
    print("Current: Voorganger")
    for nb in neighbours:
        print(nb, ":" , neighbours[nb])
            

    

if __name__ == "__main__":
    main()