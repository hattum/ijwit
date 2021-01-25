import copy
import math
from assets.helpers_miro import offsets
from classes_hattum.queue_miro import Queue
from classes_hattum.priorityqueue_miro import PriorityQueue

def is_symm(state):
    for i in range(1, len(state)):
        if state[i][1] != state[i-1][1]:
            return False
    return True

def mapper(child, string):
    childmatch = []
    for element in zip(child, string):
        pos = element[0]
        amino = element[1]
        childmatch.append((amino, pos))
    return childmatch

def map(paths, string):
    chpaths = []
    for child in paths:
        childmatch = []
        for element in zip(child, string):
            pos = element[0]
            amino = element[1]
            childmatch.append((amino, pos))
        chpaths.append(childmatch)
    return chpaths

def scoreH(child):
    scoreH = 0
    for i in range(len(child)):
        current = child[i][1]
        for j in range(i+2, len(child)):
            next = child[j][1]
            if current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and child[i][0] == "H" and child[j][0] == "H":
                scoreH += -1
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and child[i][0] == "H" and child[j][0] == "H":
                scoreH += -1
    return scoreH

#TODO: def scoreC(child):
    # scoreC = 0
    # for i in range(len(child)):
    #     current = child[i][1]
    #     for j in range(i+2, len(child)):
    #         next = child[j][1]
    #         if current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and child[i][0] == "C" and child[j][0] == "H":
    #             scoreH += -1
    #         elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and child[i][0] == "C" and child[j][0] == "H":
    #             scoreH += -1
    # return scoreC

def best_score(chpaths):
    scoreX = 0
    for chpath in chpaths:
        score = scoreH(chpath)
        if score <= scoreX:
            winner = chpath
            scoreX = score
    return winner, scoreX

def heuristic(a, b):
    """
    schuine Manhattan distance
    """
    value = value = (abs(a[0] - b[0]) * abs(a[0] - b[0])) +  (abs(a[1] - b[1]) * abs(a[1] - b[1]))
    return math.sqrt(value) * 0.2

# def has_potential(eiwit, state, depth, priority, maxscore):
#     if -(depth - len(state))* 2 <= maxscore - priority:
#     #if -(depth - len(state))* 1 <= maxscore - priority: #nieuw
#         return True
#     else:
#         return False

def has_potential(eiwit, state, depth, priority, maxscore):
    hpotentials = potentials(eiwit, depth)
    if -(hpotentials[len(state) - 1] * 3/2) <= maxscore - priority:
        return True
    else:
        return False

#TODO: def heuristic_potential(eiwit, state, depth, priority, maxscore):
#     hpotentials = potentials(eiwit, depth)
#     return -(hpotentials[len(state) - 1]* 2)

#TODO: def has_potentiaat(eiwit, state, depth, priority, maxscore):
#     cpotentials = potentiaat(eiwit)
#     if -(cpotentials[len(state) - 1]* 10) <= maxscore - priority:
#         return True
#     else:
#         return False
    
# def potentials(eiwit): #nieuw
#     hpotentials = {}
#     for i in range(len(eiwit)):
#         hpotentials[i] = 0
#         for j in range(i, len(eiwit)):
#             if eiwit[j] == "H":
#                 hpotentials[i] +=1
#     return hpotentials

def potentials(eiwit, depth): #nieuw
    hpotentials = {}
    for i in range(depth):
        hpotentials[i] = 0
        for j in range(i, depth):
            if eiwit[j] == "H":
                hpotentials[i] +=1
    return hpotentials

#TODO: def potentiaat(eiwit, depth): #nieuw
#     cpotentials = {}
#     for i in range(depth):
#         cpotentials[i] = 0
#         for j in range(i, depth):
#             if eiwit[j] == "C":
#                 cpotentials[i] +=1
#     return cpotentials


def algo(state, string, depth, maxscore, direction, paths, pq):
    neighbour_pos = (state[-1][0] + offsets[direction][0], 
                    state[-1][1] + offsets[direction][1])
    child = copy.deepcopy(state)
    if neighbour_pos not in child and child not in paths:
        child += [neighbour_pos]
        aminoschecked = string[:(len(state)+ 1)]
        #TODO: h_value = heuristic(start, neighbour_pos)
        h_value = 0
        childmatch = mapper(child, aminoschecked)
        score = scoreH(childmatch) + h_value
        if score < maxscore:
            maxscore = score
        pq.put(child, score)
        if len(child) == depth:
            paths.append(child)

def before_angle(state):
    for i in range(1, len(state)):
            if state[i][1] != state[i-1][1]:
                return i

def is_angled(state):
    i = before_angle(state)
    for j in range(i, len(state)):
        if state[j][0] != state[j-1][0]:
            return False
    return True

def make_spot_in(state):
    for i in range(1, len(state)):
            if state[i][1] != state[i-1][1]:
                return ((state[i][0] + offsets["-2"][0], 
                    state[i][1] + offsets["-2"][1]))

# def make_2nd_spot_in(state):
#     for i in range(1, len(state)):
#             if state[i][1] != state[i-1][1]:
#                 return ((state[i][0] + offsets["-2"][0], 
#                     state[i][1] + offsets["-2"][1]))  
                    
def make_spot_out(state):
    for i in range(0, len(state)):
            if state[i][1] != state[i-1][1]:
                return ((state[i-1][0] + offsets["2"][0], 
                    state[i-1][1] + offsets["2"][1]))

def has_spot_in(state, depth):
    if 3 < len(state) < depth and make_spot_in(state) not in state:
        print("State is:", state)
        print("MakeSpotIn is:", make_spot_in(state))
        return True
    else:
        return False

def has_spot_out(state, depth):
    if 3 < len(state) < depth and make_spot_out(state) not in state:
        print("State is:", state)
        print("MakeSpotOut is:", make_spot_out(state))
        return True
    else:
        return False
        

def priority_miro(depth, eiwit):
    hpotentials = potentials(eiwit, depth)
    print("Hpotentials is", hpotentials) #nieuw
    start = (0,0)
    pq = PriorityQueue()
    direction = "2"
    neighbour_pos = (start[0] + offsets[direction][0], 
                    start[1] + offsets[direction][1])
    score = 0
    maxscore = 0
    pq.put([start,neighbour_pos], score)
    paths = []
    aminoschecked = ""

    while not pq.is_empty():
        priority, state = pq.get()
        # print("state:", state)
        # print("depth:", depth)
        # print("priority:", priority)
        # print("maxscore:", maxscore)
        # print("HasPot:", has_potential(eiwit, state, depth, priority, maxscore))
        if has_potential(eiwit, state, depth, priority, maxscore): #and not (has_spot_in(state, depth) and has_spot_out(state, depth)):
            if len(state) < depth:
                if is_symm(state):
                    for direction in ["2", "1"]:
                        #TODO: algo(state, eiwit, depth, maxscore, direction, paths, pq)
                        neighbour_pos = (state[-1][0] + offsets[direction][0], 
                            state[-1][1] + offsets[direction][1])
                        child = copy.deepcopy(state)
                        if neighbour_pos not in child and child not in paths:
                            child += [neighbour_pos]
                            aminoschecked = eiwit[:(len(state)+ 1)]
                            #TODO: h_value = heuristic_potential(eiwit, state, depth, priority, maxscore)
                            #TODO: h_value = heuristic(start, neighbour_pos)
                            h_value = 0
                            childmatch = mapper(child, aminoschecked)
                            score = scoreH(childmatch) + h_value
                            if score < maxscore:
                                maxscore = score
                            pq.put(child, score)
                            if len(child) == depth:
                                paths.append(child)
                # elif is_angled(state):
                #     for direction in ["2", "-2"]:
                #         #TODO: algo(state, eiwit, depth, maxscore, direction, paths, pq)
                #         neighbour_pos = (state[-1][0] + offsets[direction][0], 
                #             state[-1][1] + offsets[direction][1])
                #         child = copy.deepcopy(state)
                #         if neighbour_pos not in child and child not in paths:
                #             child += [neighbour_pos]
                #             aminoschecked = eiwit[:(len(state)+ 1)]
                #             #TODO: h_value = heuristic(start, neighbour_pos)
                #             h_value = 0
                #             childmatch = mapper(child, aminoschecked)
                #             score = scoreH(childmatch) + h_value
                #             if score < maxscore:
                #                 maxscore = score
                #             pq.put(child, score)
                #             if len(child) == depth:
                #                 paths.append(child)

                else:
                    for direction in ["2", "1", "-2", "-1"]:
                        #TODO: algo(state, eiwit, depth, maxscore, direction, paths, pq)
                        neighbour_pos = (state[-1][0] + offsets[direction][0], 
                            state[-1][1] + offsets[direction][1])
                        child = copy.deepcopy(state)
                        if neighbour_pos not in child and child not in paths:
                            child += [neighbour_pos]
                            aminoschecked = eiwit[:(len(state)+ 1)]
                            #TODO: h_value = heuristic(start, neighbour_pos)
                            h_value = 0
                            childmatch = mapper(child, aminoschecked)
                            score = scoreH(childmatch) + h_value
                            if score < maxscore:
                                maxscore = score
                            pq.put(child, score)
                            if len(child) == depth:
                                paths.append(child)
        #print(pq.description())
    #print(f"\nPaths with depth{depth} are:", paths)
    print(f"\nLengthPaths with depth{depth} is:", len(paths))
    return paths