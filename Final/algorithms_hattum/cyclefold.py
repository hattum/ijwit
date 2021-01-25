import itertools
from assets.helpers_miro import offsets
# from classes_hattum.queue_miro import Queue
from classes_hattum.queue_miro import Queue

def mapper(child, eiwit):
        match = {}
        matcher = []
        graph = [["   " for i in range(len(eiwit))] for i in range(len(eiwit))]
        for j, element in enumerate(zip(child, eiwit)):
        #for element in zip(child, eiwit):
            pos = element[0]
            amino = element[1]
            match[pos] = amino
            matcher.append((amino, pos))
            graph[pos[0]][pos[1]] = amino +str(j)
        return match, matcher, graph

def cyclefold(eiwit):
        directs = ["2", "1", "-2", "-1"]
        directions_cycle = itertools.cycle(directs)
        start_amino = eiwit[0]
        start_pos = (0,0)
        #print("Current-ami is:",start_amino)
        #print("Current-pos is:",start_pos)
        child  = [start_pos]
        predecessors= {start_pos: None}
        directions = {}
        directions2 = []

        direction = next(directions_cycle)
        starter_amino = eiwit[1]
        neighbour_pos = (start_pos[0] + offsets[direction][0], 
                    start_pos[1] + offsets[direction][1])
        child += [neighbour_pos]
        predecessors[neighbour_pos] = start_pos
        directions[start_pos] = direction
        directions2.append((start_amino, direction))

        for i in range(2, len(eiwit)):
            direction = next(directions_cycle)
            #print("DIRECTION:",direction)
            next_amino = eiwit[i]
            print("Next-ami is:",next_amino)
            neighbour = (neighbour_pos[0] + offsets[direction][0], 
                        neighbour_pos[1] + offsets[direction][1])
            #print("Pos:", neighbour)
            if neighbour not in directions:
                #print("STARTER:", start_amino)
                directions2.append((starter_amino, direction))
                directions[neighbour_pos] = direction
                predecessors[neighbour] = neighbour_pos
                starter_amino = next_amino
                neighbour_pos = neighbour
                #print("PosValid is:",neighbour_pos)
                child.append(neighbour_pos)
                

            elif neighbour in directions:
                while neighbour in directions:
                    direction = next(directions_cycle)
                    direction = next(directions_cycle)
                    direction = next(directions_cycle)
                    directions[neighbour_pos] = direction
                    #print("OnGoing-ami is:", next_amino)
                    #print("OnGoing-pos is:",start_pos)
                    #print("DIRECTION:",direction)
                    neighbour = (neighbour_pos[0] + offsets[direction][0], 
                                neighbour_pos[1] + offsets[direction][1])
                    #print("OnGoing-ami is:", next_amino)
                    #print("Neighbour is:", neighbour)
                predecessors[neighbour] = neighbour_pos
                directions2.append((starter_amino, direction))
                directions[neighbour] = direction
                starter_amino = next_amino
                neighbour_pos = neighbour
                #print("Current-pos is:",neighbour_pos)
                child.append(neighbour_pos)
        last_amino = directions2.pop()
        laster_amino = last_amino[0]
        #print("Last amino is:", last_amino)
        laster_amino = last_amino[0]
        #print("Laster amino is:", laster_amino)
        directions2.append((laster_amino, 0))
        return child, predecessors, directions, directions2

def makeH_q(match):
        print("\nPositie: Amino-H")
        H_q = Queue()
        for amino in match:
            if match[amino] == "H":
                print(amino, ":" , match[amino])
                H_q.enqueue(amino)
        return H_q
        #print("H_q is:", H_q)
    
def makeH_lijst(match):
    Hlijst = []
    for amino in match:
        if match[amino] == "H":
            Hlijst.append(amino)
    return Hlijst
    #print("\nHlijst is:", Hlijst)

def makeC_q(match):
    print("\nPositie: Amino-C")
    C_q = Queue()
    for amino in match:
        if match[amino] == "C":
            print(amino, ":" , match[amino])
            C_q.enqueue(amino)
    return C_q
    #print("C_q is:", C_q)
    
def makeC_lijst(match):
    Clijst = []
    for amino in match:
        if match[amino] == "C":
            print(amino, ":" , match[amino])
            Clijst.append(amino)
    return Clijst
    #print("\nClijst is:", Clijst)

def scoreH(match, predecessors):
    scoreH = 0
    H_q = makeH_q(match)
    H_lijst = makeH_lijst(match)
    while not H_q.is_empty():
    #for i in range(H_q.size()):
        current_H = H_q.dequeue()
        #print("\nCurrentH is:", current_H)
        for j in range(len(H_lijst)):
        #for j in range(i+2, len(H_lijst)):
            next_H = H_lijst[j]
            # print("NextHlijst is:", next_H)
            # print("CurrentH is:", current_H)
            #print("Predecessor is:", self.predecessors[next_H])
            if current_H[0] == next_H[0] and (current_H[1] == next_H[1] - 1 or current_H[1] == next_H[1] +1) and predecessors[next_H] != current_H:
                # print("NextH_hor is:", next_H)
                # print("Predecessor is:", predecessors[next_H])
                scoreH += 1
            elif current_H[1] == next_H[1] and (current_H[0] == next_H[0] - 1 or current_H[0] == next_H[0] +1) and predecessors[next_H] != current_H:
                # print("NextH_vert is:", next_H)
                # print("Predecessor is:", predecessors[next_H])
                scoreH += 1
        H_lijst.pop(0)
    return scoreH
    # print("ScoreH is:", scoreH)

def scoreC(self):
    scoreC = 0
    C_q = makeC_q()
    C_lijst = makeC_lijst()
    for i in range(C_q.size()):
        current_C = C_q.dequeue()
        #print("CurrentC is:", current_C)
        for j in range(i+2, len(C_lijst)):
            next_C = C_lijst[j]
            #print("NextC is:", next_C)
            #print("Predecessor is:", predecessors[next_C])
            if current_C[0] == next_C[0] and (current_C[1] == next_C[1] - 1 or current_C[1] == next_C[1] +1) and self.predecessors[next_C] != current_C:
                #print("Predecessor is:", predecessors[next_C])
                #print("NextC_hor is:", next_C)
                scoreC += 5
            elif current_C[1] == next_C[1] and (current_C[0] == next_C[0] - 1 or current_C[0] == next_C[0] +1) and self.predecessors[next_C] != current_C:
                #print("NextC_vert is:", next_C)
                scoreC += 5
        return scoreC
    #print("ScoreC is:", scoreC)