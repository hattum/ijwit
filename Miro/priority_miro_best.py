import copy
from assets.helpers_miro import offsets
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
    scoreC = 0
    for i in range(len(child)):
        current = child[i][1]
        for j in range(i+2, len(child)):
            next = child[j][1]
            if current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and child[i][0] == "H" and child[j][0] == "H":
                scoreH += -1
            elif current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and child[i][0] == "C" and child[j][0] == "C":
                scoreC += -5
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and child[i][0] == "H" and child[j][0] == "H":
                scoreH += -1
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and child[i][0] == "C" and child[j][0] == "C":
                scoreC += -5
    return scoreH + scoreC


def best_score(chpaths):
    scoreX = 0
    for chpath in chpaths:
        score = scoreH(chpath)
        if score <= scoreX:
            winner = chpath
            scoreX = score
    return winner, scoreX


def potentials(eiwit, depth): #nieuw
    hpotentials = {}
    cpotentials = {}
    for i in range(0, depth):
        hpotentials[i] = 0
        cpotentials[i] = 0
        for j in range(i + 1, depth):
            if eiwit[j] == "H":
                hpotentials[i] +=1
            elif eiwit[j] == "C":
                cpotentials[i] += 5
    return hpotentials, cpotentials


def priority_miro(depth, eiwit):
    hpotentials, cpotentials = potentials(eiwit, depth)
    print("Hpotentials is", hpotentials) #nieuw
    print("Cpotentials is", cpotentials) #nieuw
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
        print("\ndepthbefore:", depth)
        print("prioritybefore:", priority)
        print("maxscorebefore:", maxscore)
        print("state:", state)
        if len(state) < depth:
            if is_symm(state):
                for direction in ["2", "1"]:
                    #TODO: algo(state, eiwit, depth, maxscore, direction, paths, pq)
                    neighbour_pos = (state[-1][0] + offsets[direction][0], 
                        state[-1][1] + offsets[direction][1])
                    child = copy.deepcopy(state)
                    if neighbour_pos not in child and child not in paths:
                        child += [neighbour_pos]
                        print("\nChild is:", child)
                        aminoschecked = eiwit[:(len(state)+ 1)]
                        childmatch = mapper(child, aminoschecked)
                        print("Hpotentials[len(child) - 1] is:", hpotentials[len(child) - 1])
                        print("Cpotentials[len(child) - 1] is:", cpotentials[len(child) - 1])
                        h_value = -((hpotentials[len(child) - 1]) * 4/3)-((cpotentials[len(child) - 1]) * 4/3)
                        print("H+Cvalue is:", h_value)
                        score = scoreH(childmatch)
                        print("Score is:", score)
                        priority = score + h_value
                        print("Priority is:", priority)
                        print("maxscoretervergelijk:", maxscore)
                        if priority <= maxscore:
                            pq.put(child, priority)
                        if score < maxscore:
                            maxscore = score
                        if len(child) == depth:
                            paths.append(child)

            else:
                for direction in ["2", "1", "-2", "-1"]:
                    #TODO: algo(state, eiwit, depth, maxscore, direction, paths, pq)
                    neighbour_pos = (state[-1][0] + offsets[direction][0], 
                        state[-1][1] + offsets[direction][1])
                    child = copy.deepcopy(state)
                    if neighbour_pos not in child and child not in paths:
                        child += [neighbour_pos]
                        print("\nChild is:", child)
                        aminoschecked = eiwit[:(len(state)+ 1)]
                        childmatch = mapper(child, aminoschecked)
                        print("Hpotentials[len(child) - 1] is:", hpotentials[len(child) - 1])
                        print("Cpotentials[len(child) - 1] is:", cpotentials[len(child) - 1])
                        h_value = -((hpotentials[len(child) - 1]) * 4/3)-((cpotentials[len(child) - 1]) * 4/3)
                        print("H+Cpotentie is:", h_value)
                        score = scoreH(childmatch)
                        print("Score is:", score)
                        priority = score + h_value
                        print("Priority is:", priority)
                        print("maxscoretervergelijk:", maxscore)
                        if priority <= maxscore:
                            pq.put(child, priority)
                        if score < maxscore:
                            maxscore = score
                        if len(child) == depth:
                            paths.append(child)
        #print(pq.description())
    #print(f"\nPaths with depth{depth} are:", paths)
    print(f"\nLengthPaths with depth{depth} is:", len(paths))
    return paths

# def algo(state, eiwit, depth, maxscore, direction, paths, pq):
#     neighbour_pos = (state[-1][0] + offsets[direction][0], 
#                     state[-1][1] + offsets[direction][1])
#     child = copy.deepcopy(state)
#     if neighbour_pos not in child and child not in paths:
#         child += [neighbour_pos]
#         print("\nChild is:", child)
#         aminoschecked = eiwit[:(len(state)+ 1)]
#         childmatch = mapper(child, aminoschecked)
#         print("Hpotentials[len(child) - 1] is:", hpotentials[len(child) - 1])
#         print("Cpotentials[len(child) - 1] is:", cpotentials[len(child) - 1])
#         h_value = -((hpotentials[len(child) - 1]) * 4/3)-((cpotentials[len(child) - 1]) * 4/3)
#         print("H+Cvalue is:", h_value)
#         score = scoreH(childmatch)
#         print("Score is:", score)
#         priority = score + h_value
#         print("Priority is:", priority)
#         print("maxscoretervergelijk:", maxscore)
#         if priority <= maxscore:
#             pq.put(child, priority)
#         if score < maxscore:
#             maxscore = score
#         if len(child) == depth:
#             paths.append(child)

