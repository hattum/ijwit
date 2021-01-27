import copy
from assets.helpers_miro import offsets
from classes_hattum.priorityqueue_miro import PriorityQueue


def is_symm(state):
    """
    check if the current state is vertically aligned
    """
    for i in range(1, len(state)):
        if state[i][1] != state[i-1][1]:
            return False
    return True


def mapper(coords, eiwit):
    """
    map the assigned coordinates with the aminos
    """
    coordsmatch = []
    for element in zip(coords, eiwit):
        pos = element[0]
        amino = element[1]
        coordsmatch.append((amino, pos))
    return coordsmatch

def map(paths, eiwit):
    """
    map the assigned coordinates with the aminos of all possible paths
    """
    pathsmatch = []
    for child in paths:
        childmatch = mapper(child, eiwit)
        pathsmatch.append(childmatch)
    return pathsmatch


def scoreH(coordsmatch):
    """
    returns score of all bonds among the assigned coordinates of a single proteine
    """
    scoreH = 0
    scoreC = 0
    for i in range(len(coordsmatch)):
        current = coordsmatch[i][1]
        for j in range(i+2, len(coordsmatch)):
            next = coordsmatch[j][1]
            if current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and coordsmatch[i][0] == "H" and (coordsmatch[j][0] == "H" or coordsmatch[j][0] == "C"):
                scoreH += -1
            elif current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and coordsmatch[i][0] == "C" and coordsmatch[j][0] == "C":
                scoreC += -5
            elif current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and coordsmatch[i][0] == "C" and coordsmatch[j][0] == "H":
                scoreC += -1
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and coordsmatch[i][0] == "H" and (coordsmatch[j][0] == "H" or coordsmatch[j][0] == "C"):
                scoreH += -1
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and coordsmatch[i][0] == "C" and coordsmatch[j][0] == "C":
                scoreC += -5
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and coordsmatch[i][0] == "C" and coordsmatch[j][0] == "H":
                scoreC += -1
    return scoreH + scoreC


def best_score(paths):
    """
    returns a single winner and related best_score out of all possible paths
    """
    bestscore = 0
    for path in paths:
        score = scoreH(path)
        if score <= bestscore:
            winner = path
            bestscore = score
    try:
        return winner, bestscore
    except:
        raise Exception("score was not in range")


def potentials(eiwit, depth):
    """
    make registers of potential scores of bonds
    """
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


def factor(eiwit, depth):
    """
    calculate the number of H's and C's and divide by the set depth
    """
    count = 0
    for i in range(0, depth):
        if eiwit[i] == "H" or eiwit[i] == "C":
            count += 1
    return count/depth


def get_heuristic(eiwit, child, hpotentials, cpotentials, depth, cyclevalue, heuristic):
    """
    returns the heuristic value related to the unfolding of the proteine so far.
    the heuristic value refers to the potential scores of upcoming bonds if unfolding proceeds
    """
    if heuristic == "admissable":
        return -((hpotentials[len(child) - 1]) * 2) - ((cpotentials[len(child) - 1]) * 5)
    if heuristic == "regular":
        return -((hpotentials[len(child) - 1]) * ((depth + 1)/depth)) - ((cpotentials[len(child) - 1]) * ((depth + 1)/depth))
    if heuristic == "cyclebased":
        return -((hpotentials[len(child) - 1]) * (-cyclevalue/depth)) - ((cpotentials[len(child) - 1]) * (-cyclevalue/depth))
    if heuristic == "cyclereducedbyfactor":
        number = factor(eiwit, depth)
        return -((hpotentials[len(child) - 1]) * (-cyclevalue/depth)) - ((cpotentials[len(child) - 1]) * (-cyclevalue/depth)) * number


def priority_miro(depth, eiwit, cyclevalue, heuristic, hpotentials, cpotentials, pq, maxscore, paths):
    """
    keep on making children from every state of the family and accept the children only
    if they could still transcend the maxscore so far in the family
    """
    while not pq.is_empty():
        state = pq.get()
        if len(state) < depth:
            if is_symm(state):
                directions = ["2", "1"]
            else:
                directions =["2", "1", "-2", "-1"]

            for direction in directions:
                neighbour_pos = (state[-1][0] + offsets[direction][0], 
                    state[-1][1] + offsets[direction][1])
                child = copy.deepcopy(state)
                if neighbour_pos not in child and child not in paths:
                    child += [neighbour_pos]
                    aminoschecked = eiwit[:(len(state)+ 1)]
                    childmatch = mapper(child, aminoschecked)
                    h_value = get_heuristic(eiwit, state, hpotentials, cpotentials, depth, cyclevalue, heuristic)
                    score = scoreH(childmatch)
                    priority = score + h_value
                    if priority <= maxscore:
                        pq.put(child, priority)
                    if score < maxscore:
                        maxscore = score
                    if len(child) == depth:
                        paths.append(child)
    
    return paths
    


        

