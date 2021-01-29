import copy
import itertools
from assets.helpers_miro import offsets


class CycleFold():
    """
    Hardcode the first 2 coordinates when Initializing the class
    """
    def __init__(self, eiwit):
        self.eiwit = eiwit
        self.coords = [(0,0),(-1,0)]
        self.directs = ["1", "-2", "-1", "2"]
        self.directions_cycle = itertools.cycle(self.directs)


    def cyclefolder(self):
        """
        'Cyclefold' folds the protein clockwise around his center.
        """
        for i in range(2, len(self.eiwit)):
            direction = next(self.directions_cycle)
            neighbour = (self.coords[-1][0] + offsets[direction][0], 
                        self.coords[-1][1] + offsets[direction][1])
            if neighbour not in self.coords:
                neighbour_pos = neighbour
                self.coords.append(neighbour_pos)
            elif neighbour in self.coords:
                while neighbour in self.coords:
                    direction = next(self.directions_cycle)
                    direction = next(self.directions_cycle)
                    direction = next(self.directions_cycle)
                    neighbour = (neighbour_pos[0] + offsets[direction][0], 
                                neighbour_pos[1] + offsets[direction][1])
                neighbour_pos = neighbour
                self.coords.append(neighbour_pos)
        

    def run(self):
        self.cyclefolder()


    def score(self):
            """
            make match among all possible paths and the proteine and return winner, best_score
            """
            self.matcher = mapper(self.coords, self.eiwit)
            return scoreHC(self.matcher)


    def coord(self):
            """
            return coordinates of the proteine folding
            """
            return self.matcher

def mapper(coords, eiwit):
    """
    Map the retrieved coordinates with the input proteine-string
    """

    matcher = []
    for element in zip(coords, eiwit):
        pos = element[0]
        amino = element[1]
        matcher.append((amino, pos))
    return matcher


def scoreHC(coordsmatch):
    """
    returns score of all bonds among the assigned coordinates of a single proteine
    """
    scoreH = 0
    scoreC = 0
    for i in range(len(coordsmatch)):
        current = coordsmatch[i][1]
        for j in range(i+2, len(coordsmatch)):
            next = coordsmatch[j][1]
            if current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and coordsmatch[i][0] == "H" and coordsmatch[j][0] == "H":
                scoreH += -1
            elif current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and coordsmatch[i][0] == "H" and coordsmatch[j][0] == "C":
                scoreH += -1
            elif current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and coordsmatch[i][0] == "C" and coordsmatch[j][0] == "C":
                scoreC += -5
            elif current[0] == next[0] and (current[1] == next[1] - 1 or current[1] == next[1] +1) and coordsmatch[i][0] == "C" and coordsmatch[j][0] == "H":
                scoreC += -1
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and coordsmatch[i][0] == "H" and coordsmatch[j][0] == "H":
                scoreH += -1
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and coordsmatch[i][0] == "H" and coordsmatch[j][0] == "C":
                scoreH += -1
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and coordsmatch[i][0] == "C" and coordsmatch[j][0] == "C":
                scoreC += -5
            elif current[1] == next[1] and (current[0] == next[0] - 1 or current[0] == next[0] +1) and coordsmatch[i][0] == "C" and coordsmatch[j][0] == "H":
                scoreC += -1
    return scoreH + scoreC
