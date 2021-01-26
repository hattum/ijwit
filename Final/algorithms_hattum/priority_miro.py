import copy
from assets.helpers_miro import offsets
from classes_hattum.priorityqueue_miro import PriorityQueue

"""
'Priority' vouwt een 'eiwit' en geeft een lijst 'paths' met daarin
lijsten van coordinaten.
'Mapper' mapt de 'coords' met het 'eiwit' en geeft lijst 'matcher'.
'ScoreHC' geeft de score van de vouwing.
'Is_symm' checkt of de voorgaande coordinaten in een rechte lijn liggen.
'Mapper' mapt de 'coords' met het 'eiwit' tot een lijst 'coordsmatch'
'Map' mapt alle 'paths' met het 'eiwit' tot een lijst 'pathsmatch'
'ScoreH' geeft de totaalscore van de vouwing.
'Best_score' geeft de beste scoorder en score.
'Best_scoorders' geeft een lijst vd beste scoorders en een lijst vd resp scores.
'Potentials' geeft zowel 'hpotentials' als 'cpotentials'.
'Hpotentials' is een dictionary vd hoeveelheid H's die nog moeten komen per index vd 'depth'
'Cpotentials' is een dictionary vd hoeveelheid C's die nog moeten komen per index vd 'depth'
"""
def directions(coords):
    dict = {}
    for i in range(len(coords) - 1):
        for direction in offsets:
            if coords[i+1][1] == (coords[i][1][0] + offsets[direction][0], 
                        coords[i][1][1] + offsets[direction][1]):
                dict[coords[i][0]] = direction
    dict[coords[-1][0]] = "0"
    return dict

def countinvalids(eiwit, depth):
    omgekeerd = ''.join(reversed(eiwit[:depth]))
    invalids = ''
    print(omgekeerd)
    for ch in omgekeerd:
        if ch == "H" or ch == "C":
            break
        else:
            invalids += ch
    return len(invalids)

def is_symm(state):
    for i in range(1, len(state)):
        if state[i][1] != state[i-1][1]:
            return False
    return True


def mapper(coords, eiwit):
    coordsmatch = []
    for element in zip(coords, eiwit):
        pos = element[0]
        amino = element[1]
        coordsmatch.append((amino, pos))
    return coordsmatch

def map(paths, eiwit):
    pathsmatch = []
    for child in paths:
        childmatch = []
        for element in zip(child, eiwit):
            pos = element[0]
            amino = element[1]
            childmatch.append((amino, pos))
        pathsmatch.append(childmatch)
    return pathsmatch


def scoreH(coordsmatch):
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
    scoreX = 0
    for path in paths:
        score = scoreH(path)
        if score <= scoreX:
            winner = path
            scoreX = score
    try:
        return winner, scoreX
    except:
        raise Exception("score was not in range")

def best_scoorders(paths):
    scoorders = []
    scoreX = 0
    scores = []
    for path in paths:
        score = scoreH(path)
        if score <= scoreX:
            scoorders.append(path)
            scores.append(score)
            scoreX = score
    return scoorders, scores


def potentials(eiwit, depth):
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
    count = 0
    for i in range(0, depth):
        if eiwit[i] == "H" or eiwit[i] == "C":
            count += 1
    return count/depth


def algo(state, eiwit, depth, maxscore, direction, paths, pq, hpotentials, cpotentials, heuristic):
    neighbour_pos = (state[-1][0] + offsets[direction][0], 
                        state[-1][1] + offsets[direction][1])
    child = copy.deepcopy(state)
    if neighbour_pos not in child and child not in paths:
        child += [neighbour_pos]
        aminoschecked = eiwit[:(len(state)+ 1)]
        childmatch = mapper(child, aminoschecked)
        if heuristic == "admissable":
            h_value = -((hpotentials[len(child) - 1]) * 2) - ((cpotentials[len(child) - 1]) * 5)
        if heuristic == "regular":
            h_value = -((hpotentials[len(child) - 1]) * ((depth + 1)/depth)) - ((cpotentials[len(child) - 1]) * ((depth + 1)/depth))
        if heuristic == "cyclebased":
            h_value = -((hpotentials[len(child) - 1]) * (-cyclevalue/depth)) - ((cpotentials[len(child) - 1]) * (-cyclevalue/depth))
        if heuristic == "cyclereducedbyfactor": 
            h_value = -((hpotentials[len(child) - 1]) * (-cyclevalue/depth)) - ((cpotentials[len(child) - 1]) * (-cyclevalue/depth)) * factor
        score = scoreH(childmatch)
        priority = score + h_value
        if priority <= maxscore:
            pq.put(child, priority)
        if score < maxscore:
            maxscore = score
        if len(child) == depth:
            paths.append(child)


def priority_miro(depth, eiwit, cyclevalue, heuristic, hpotentials, cpotentials, pq, maxscore, paths):
    while not pq.is_empty():
        priority, state = pq.get()
        if len(state) < depth:
            if is_symm(state):
                for direction in ["2", "1"]:
                    #algo(state, eiwit, depth, maxscore, direction, paths, pq, hpotentials, cpotentials, heuristic)
                    neighbour_pos = (state[-1][0] + offsets[direction][0], 
                        state[-1][1] + offsets[direction][1])
                    child = copy.deepcopy(state)
                    if neighbour_pos not in child and child not in paths:
                        child += [neighbour_pos]
                        aminoschecked = eiwit[:(len(state)+ 1)]
                        childmatch = mapper(child, aminoschecked)
                        if heuristic == "admissable":
                            h_value = -((hpotentials[len(child) - 1]) * 2) - ((cpotentials[len(child) - 1]) * 5)
                        if heuristic == "regular":
                            h_value = -((hpotentials[len(child) - 1]) * ((depth + 1)/depth)) - ((cpotentials[len(child) - 1]) * ((depth + 1)/depth))
                        if heuristic == "cyclebased":
                            h_value = -((hpotentials[len(child) - 1]) * (-cyclevalue/depth)) - ((cpotentials[len(child) - 1]) * (-cyclevalue/depth))
                        if heuristic == "cyclereducedbyfactor": 
                            h_value = -((hpotentials[len(child) - 1]) * (-cyclevalue/depth)) - ((cpotentials[len(child) - 1]) * (-cyclevalue/depth)) * factor
                        score = scoreH(childmatch)
                        priority = score + h_value
                        if priority <= maxscore:
                            pq.put(child, priority)
                        if score < maxscore:
                            maxscore = score
                        if len(child) == depth:
                            paths.append(child)
                        

            else:
                for direction in ["2", "1", "-2", "-1"]:
                    #algo(state, eiwit, depth, maxscore, direction, paths, pq, hpotentials, cpotentials, heuristic)
                    neighbour_pos = (state[-1][0] + offsets[direction][0], 
                        state[-1][1] + offsets[direction][1])
                    child = copy.deepcopy(state)
                    if neighbour_pos not in child and child not in paths:
                        child += [neighbour_pos]
                        print("\nChild is:", child)
                        aminoschecked = eiwit[:(len(state)+ 1)]
                        childmatch = mapper(child, aminoschecked)
                        if heuristic == "admissable":
                            h_value = -((hpotentials[len(child) - 1]) * 2) - ((cpotentials[len(child) - 1]) * 2)
                        if heuristic == "regular":
                            h_value = -((hpotentials[len(child) - 1]) * ((depth + 1)/depth)) - ((cpotentials[len(child) - 1]) * ((depth + 1)/depth))
                        if heuristic == "cyclebased":
                            h_value = -((hpotentials[len(child) - 1]) * (-cyclevalue/depth)) - ((cpotentials[len(child) - 1]) * (-cyclevalue/depth))
                        if heuristic == "cyclereducedbyfactor": 
                            h_value = -((hpotentials[len(child) - 1]) * (-cyclevalue/depth)) - ((cpotentials[len(child) - 1]) * (-cyclevalue/depth)) * factor
                        score = scoreH(childmatch)
                        priority = score + h_value
                        if priority <= maxscore:
                            pq.put(child, priority)
                        if score < maxscore:
                            maxscore = score
                        if len(child) == depth:
                            paths.append(child)
                        

    #print(f"\nPaths with depth{depth} are:", paths)
    #print(f"\nLengthPaths with depth{depth} is:", len(paths))
    return paths


        

