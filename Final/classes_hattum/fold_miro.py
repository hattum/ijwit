import copy
import itertools
from classes_hattum.priorityqueue_miro import PriorityQueue
from assets.helpers_miro import offsets
from algorithms_hattum.cyclefold import cyclefold, mapper, scoreHC
from algorithms_hattum.priority_miro import priority_miro, map, best_scoorders, best_score, potentials
#from algorithms_hattum.priority_miro import Priority, map, best_score
from classes_hattum.priorityqueue_miro import PriorityQueue

class Fold():
    """
    Parent Fold heeft 'eiwit' en 'algorithm' als attributen
    """
    def __init__(self, eiwit):
        self.eiwit = eiwit
        
        
class PriorityFold(Fold):
    """
    Child PriortyFold heeft 'depth' als attribuut. Elk lijst coordinaten uit lijst 'paths' bestaat
    uit getupelde coordinaten die algoritme 'priority' heeft gemaakt. Elke lijst karakterspad uit
    lijst 'pathsmatch' bestaat uit tuples van een aminozuur met zijn gemapte getupelde coordinaten.
    'Score' is een methode die de vouwing van het eiwit met de meeste bonds geeft.
    """

    def __init__(self, eiwit, depth, cyclevalue, heuristic):
        super().__init__(eiwit)
        self.depth = depth
        self.cyclevalue = cyclevalue
        self.heuristic = heuristic
        self.hpotentials, self.cpotentials = potentials(self.eiwit, self.depth) #nieuw
        self.pq = PriorityQueue()
        self.pq.put([(0,0),(-1,0)], 0)
        self.maxscore = 0
        self.paths = []
        self.coords = priority_miro(self.depth, self.eiwit, self.cyclevalue, self.heuristic, self.hpotentials, self.cpotentials, self.pq, self.maxscore, self.paths)
        self.pathsmatch = map(self.coords, self.eiwit)

    def score(self):
        return best_score(self.pathsmatch)

    def scoorders(self):
        return best_scoorders(self.pathsmatch)

class CycleFold(Fold):
    """
    De 'coordinates' (en overige attributen) van het kind CycleFold komen door middels het algoritme 'cyclefold'
    die het 'eiwit' als parameter neemt en/of zijn een mapping tussen de coordinaten en het eiwit.
    """
    def __init__(self, eiwit):
        super().__init__(eiwit)
        self.coordinates, self.directions2 = cyclefold(self.eiwit)
        self.matcher = mapper(self.coordinates, self.eiwit)

    def score(self):
        return scoreHC(self.matcher)

    def printDirections(self):
        print("\nCurrAmi: Richting")
        for tupler in range(len(self.directions2)):
            print(self.directions2[tupler][0], ",", self.directions2[tupler][1])

    def coord(self):
        return self.matcher

