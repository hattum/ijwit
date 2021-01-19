import copy
import math
from helpers_miro import offsets
from queue_miro import Queue, AminoQueue
from priorityqueue_miro import PriorityQueue

def is_symm(state):
    for i in range(1, len(state)):
        if state[i][1] != state[i-1][1]:
            return False
    return True

def before_angle(state):
    for i in range(1, len(state)):
            if state[i][1] != state[i-1][1]:
                return i

def is_angled(state):
    i = before_angle(state)
    for i in range(i, len(state)):
        if state[i][0] != state[i-1][0]:
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

def priority_miro(depth):
    start = (0,0)
    #string = "HHPHHHPH" #8
    string = "HHPHHHPHPHHHPH" #14
    #string = "HPHPPHHPHPPHPHHPPHPH" #20
    pq = PriorityQueue()
    direction = "2"
    neighbour_pos = (start[0] + offsets[direction][0], 
                    start[1] + offsets[direction][1])
    score = 0
    maxscore = 0
    pq.put([start,neighbour_pos], score)
    paths = []
    aminoschecked = string[0] + string[1]

    while not pq.is_empty():
        print(pq.description())
        #TODO: priority = pq.getpriority()
        state = pq.get()
        print("LastState is:", state)
        if len(state) < depth:
            if is_symm(state):
                for direction in ["2", "1"]:
                    neighbour_pos = (state[-1][0] + offsets[direction][0], 
                                    state[-1][1] + offsets[direction][1])
                    child = copy.deepcopy(state)
                    if neighbour_pos not in child and child not in paths:
                        child += [neighbour_pos]
                        aminoschecked = string[:(len(state)+ 1)]
                        h_value = heuristic(start, neighbour_pos)
                        #h_value = 0
                        childmatch = mapper(child, aminoschecked)
                        score = scoreH(childmatch) + h_value
                        if score < maxscore: #heuristic()
                            maxscore = score
                            print("Maxscore is:", maxscore)
                        print("ScoreHIER is:", score)
                        pq.put(child, score)
                        if len(child) == depth:
                            if -(depth - len(aminoschecked)) * 2 <= maxscore - score:
                                paths.append(child)

            elif is_angled(state):
                for direction in ["2", "-2"]:
                    neighbour_pos = (state[-1][0] + offsets[direction][0], 
                                    state[-1][1] + offsets[direction][1])
                    child = copy.deepcopy(state)
                    if neighbour_pos not in child and child not in paths:
                        child += [neighbour_pos]
                        aminoschecked = string[:(len(state)+ 1)]
                        h_value = heuristic(start, neighbour_pos)
                        #h_value = 0
                        childmatch = mapper(child, aminoschecked)
                        score = scoreH(childmatch) + h_value
                        if score < maxscore:
                            maxscore = score
                            print("Maxscore is:", maxscore)
                        print("ChildHIERHIER is:", child)
                        print("ScoreHIERHIER is:", score)
                        pq.put(child, score)
                        if len(child) == depth:
                            if -(depth - len(aminoschecked)) * 2 <= maxscore - score:
                                paths.append(child)
                        
            else:
                for direction in ["2", "1", "-2", "-1"]:
                    neighbour_pos = (state[-1][0] + offsets[direction][0], 
                        state[-1][1] + offsets[direction][1])
                    child = copy.deepcopy(state)
                    if neighbour_pos not in child and child not in paths:
                        child += [neighbour_pos]
                        aminoschecked = string[:(len(state)+ 1)]
                        h_value = heuristic(start, neighbour_pos)
                        #h_value = 0
                        childmatch = mapper(child, aminoschecked)
                        score = scoreH(childmatch) + h_value
                        if score < maxscore:
                            maxscore = score
                            print("Maxscore is:", maxscore)
                        pq.put(child, score)
                        if len(child) == depth:
                            if -(depth - len(aminoschecked)) * 2 <= maxscore - score:
                                paths.append(child)

    print(f"\nPaths with depth{depth} are:", paths)
    print(f"\nLengthPaths with depth{depth} is:", len(paths))

    chpaths = map(paths, string)
    #print(f"chpaths with depth{depth} are:", chpaths)
    print(f"LengthChpaths with depth{depth} is:", len(chpaths))

    winner, scoreX = best_score(chpaths)
    print("\nBestChild is:", winner)
    print("BestScore is:", scoreX)


def main():

    print(priority_miro(14))
    #print(priority_miro(8))

if __name__ == "__main__":
    main()
    