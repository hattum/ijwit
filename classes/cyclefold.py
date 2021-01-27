import copy
import itertools
from assets.helpers_miro import offsets


class CycleFold():
    """
    De 'coordinates' (en overige attributen) van het kind CycleFold komen door middels het algoritme 'cyclefold'
    die het 'eiwit' als parameter neemt en/of zijn een mapping tussen de coordinaten en het eiwit.
    """
    def __init__(self, eiwit):
        self.eiwit = eiwit
        self.coords = [(0,0),(-1,0)]
        self.directs = ["1", "-2", "-1", "2"]
        self.directions_cycle = itertools.cycle(self.directs)


    def cyclefolder(self):
        """
        'Cyclefold' vouwt een 'eiwit' rechtsom en geeft een lijst van 'coords'.
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


def scoreHC(child):
    """
    calculate score of the cyclefolded proteine
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
