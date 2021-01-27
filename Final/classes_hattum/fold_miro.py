import copy
import itertools
from classes_hattum.priorityqueue_miro import PriorityQueue
from assets.helpers_miro import offsets
from algorithms_hattum.cyclefold import cyclefold, mapper, scoreHC
from algorithms_hattum.priority_miro import priority_miro, best_score, potentials, map
from classes_hattum.priorityqueue_miro import PriorityQueue

class Fold():
    """
    Parent Fold heeft 'eiwit' als attribuut
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


class CycleFold(Fold):
    """
    De 'coordinates' (en overige attributen) van het kind CycleFold komen door middels het algoritme 'cyclefold'
    die het 'eiwit' als parameter neemt en/of zijn een mapping tussen de coordinaten en het eiwit.
    """
    def __init__(self, eiwit):
        super().__init__(eiwit)
        self.coords = [(0,0),(-1,0)]
        self.directs = ["1", "-2", "-1", "2"]
        self.directions_cycle = itertools.cycle(self.directs)
        self.coordinates = cyclefold(self.eiwit, self.coords, self.directions_cycle)
        self.matcher = mapper(self.coordinates, self.eiwit)

    def score(self):
        return scoreHC(self.matcher)

    def coord(self):
        return self.matcher

