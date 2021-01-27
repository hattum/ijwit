import itertools
from assets.helpers_miro import offsets
from classes_hattum.queue_miro import Queue


def cyclefold(eiwit, coords, directions_cycle):

    """
    'Cyclefold' vouwt een 'eiwit' rechtsom en geeft een lijst van 'coords'.
    """
    for i in range(2, len(eiwit)):
        direction = next(directions_cycle)
        neighbour = (coords[-1][0] + offsets[direction][0], 
                    coords[-1][1] + offsets[direction][1])
        if neighbour not in coords:
            neighbour_pos = neighbour
            coords.append(neighbour_pos)
        elif neighbour in coords:
            while neighbour in coords:
                direction = next(directions_cycle)
                direction = next(directions_cycle)
                direction = next(directions_cycle)
                neighbour = (neighbour_pos[0] + offsets[direction][0], 
                            neighbour_pos[1] + offsets[direction][1])
            neighbour_pos = neighbour
            coords.append(neighbour_pos)
    return coords


def mapper(coords, eiwit):
    """
    'Mapper' mapt de 'coords' met het 'eiwit' en geeft lijst 'matcher
    """

    matcher = []
    for element in zip(coords, eiwit):
        pos = element[0]
        amino = element[1]
        matcher.append((amino, pos))
    return matcher


def scoreHC(child):
    """
    'ScoreHC' geeft de score van de vouwing.
    """
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


