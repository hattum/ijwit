import itertools
from queue_miro import Queue
from priorityqueue_miro import PriorityQueue
from collections import OrderedDict

offsets = OrderedDict()
offsets = {
    "1": [0, 1],
    "-1": [0, -1],
    "2": [-1, 0],
    "-2": [1, 0]
}

# offsets = {
#     "right": (0, 1),
#     "left": (0, -1),
#     "up": (-1, 0),
#     "down": (1, 0)
# }

# class Aminostring:
#     def __init__(self, amino_string):
#         self.amino_string = amino_string

    # def cyclesearch(self):
    #     directs = ["2", "1", "-2", "-1"]
    #     directions_cycle = itertools.cycle(directs)
    #     amino_q = Queue()
    #     amino_q.fill_que(self.amino_string)
    #     start_amino = amino_q.dequeue()
    #     current_pos = (int(len(self.amino_string)/2) - 1,int(len(self.amino_string)/2) - 1)
    #     print("Current-ami is:",start_amino)
    #     print("Current-pos is:",current_pos)
    #     amino_poss = [current_pos]
    #     predecessors= {current_pos: None}
    #     directions = {}

    #     while not amino_q.is_empty():
    #         direction = next(directions_cycle)
    #         directions[current_pos] = direction
    #         print("DIRECTION:",direction)
    #         next_amino = amino_q.dequeue()
    #         print("Next-ami is:",next_amino)
    #         neighbour = (current_pos[0] + offsets[direction][0], 
    #                     current_pos[1] + offsets[direction][1])
    #         print("Pos:", neighbour)
    #         if neighbour not in directions:
    #             directions[current_pos] = direction
    #             predecessors[neighbour] = current_pos
    #             current_pos = neighbour
    #             print("PosValid is:",current_pos)
    #             amino_poss.append(current_pos)
                
            
    #         elif neighbour in directions:
    #             while neighbour in directions:
    #                 direction = next(directions_cycle)
    #                 directions[current_pos] = direction
    #                 print("OnGoing-ami is:", next_amino)
    #                 print("OnGoing-pos is:",current_pos)
    #                 print("DIRECTION:",direction)
    #                 neighbour = (current_pos[0] + offsets[direction][0], 
    #                             current_pos[1] + offsets[direction][1])
    #                 print("OnGoing-ami is:", next_amino)
    #                 print("Neighbour is:", neighbour)
    #             predecessors[neighbour] = current_pos
    #             directions[neighbour] = direction
    #             current_pos = neighbour
    #             print("Current-pos is:",current_pos)
    #             amino_poss.append(current_pos)
    #     return amino_poss, predecessors, directions

    # def score(self):
    #     #match = {}
    #     amino_poss = self.cyclesearch()
    #     for j, element in enumerate(zip(amino_poss, list(self.amino_string))):
    #         pos = element[0]
    #         amino = element[1]
    #         match[pos] = amino
    #         #graph[pos[0]][pos[1]] = amino+str(j)
    #         #graph[pos[0]][pos[1]] = amino
    #         print("\nPositie: Amino-H")

    #     H_q = Queue()
    #     for amino in match:
    #         if match[amino] == "H":
    #             print(amino, ":" , match[amino])
    #             H_q.enqueue(amino)
    #     print("H_q is:", H_q)

    #     Hlijst = []
    #     for amino in match:
    #         if match[amino] == "H":
    #             print(amino, ":" , match[amino])
    #             Hlijst.append(amino)
    #     print("Hlijst is:", Hlijst)

    #     for i in range(H_q.size()):
    #         current_H = H_q.dequeue()
    #         print("CurrentH is:", current_H)
    #         for j in range(i+2, len(Hlijst)):
    #             next_H = Hlijst[j]
    #             print("NextH is:", next_H)
    #             print("Predecessor is:", predecessors[next_H])
    #             if current_H[0] == next_H[0] and (current_H[1] == next_H[1] - 1 or current_H[1] == next_H[1] +1) and predecessors[next_H] != current_H:
    #                 print("Predecessor is:", predecessors[next_H])
    #                 print("NextH_hor is:", next_H)
    #                 score += 1
    #             elif current_H[1] == next_H[1] and (current_H[0] == next_H[0] - 1 or current_H[0] == next_H[0] +1) and predecessors[next_H] != current_H:
    #                 print("NextH_vert is:", next_H)
    #                 score += 1
    #     return score

