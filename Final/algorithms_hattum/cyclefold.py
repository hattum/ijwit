import itertools
from assets.helpers_miro import offsets
from classes_hattum.queue_miro import Queue

"""
'Cyclefold' vouwt een 'eiwit' rechtsom en geeft een lijst van 'coords'.
'Mapper' mapt de 'coords' met het 'eiwit' en geeft lijst 'matcher'.
'ScoreHC' geeft de score van de vouwing.
"""

def cyclefold(eiwit):
        directs = ["1", "-2", "-1", "2"]
        directions_cycle = itertools.cycle(directs)
        predecessors= {(0,0): None, (-1,0): (0,0)}
        directions = {(0,0): "2"}
        directions2 = [(eiwit[0], "2")]
        starter_amino = eiwit[1]
        neighbour_pos = (-1,0)
        coords = [(0,0),(-1,0)]

        for i in range(2, len(eiwit)):
            direction = next(directions_cycle)
            next_amino = eiwit[i]
            neighbour = (neighbour_pos[0] + offsets[direction][0], 
                        neighbour_pos[1] + offsets[direction][1])
            if neighbour not in directions:
                directions2.append((starter_amino, direction))
                directions[neighbour_pos] = direction
                predecessors[neighbour] = neighbour_pos
                starter_amino = next_amino
                neighbour_pos = neighbour
                coords.append(neighbour_pos)
            elif neighbour in directions:
                while neighbour in directions:
                    direction = next(directions_cycle)
                    direction = next(directions_cycle)
                    direction = next(directions_cycle)
                    directions[neighbour_pos] = direction
                    neighbour = (neighbour_pos[0] + offsets[direction][0], 
                                neighbour_pos[1] + offsets[direction][1])
                predecessors[neighbour] = neighbour_pos
                directions2.append((starter_amino, direction))
                directions[neighbour] = direction
                starter_amino = next_amino
                neighbour_pos = neighbour
                coords.append(neighbour_pos)
        directions2.append((next_amino, "0"))
        return coords, directions2


def mapper(coords, eiwit):
        matcher = []
        for element in zip(coords, eiwit):
            pos = element[0]
            amino = element[1]
            matcher.append((amino, pos))
        return matcher


def scoreHC(child):
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


