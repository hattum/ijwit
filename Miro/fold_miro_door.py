import copy
import itertools
from classes_hattum.priorityqueue_miro import PriorityQueue
from assets.helpers_miro import offsets
from algorithms_hattum.cyclefold import cyclefold, mapper, scoreH
#from algorithms_hattum.priority_miro import priority_miro, map, best_score
from algorithms_hattum.priority_miro import priority_miro, map, best_scoorders
#from algorithms_hattum.priority_miro import Priority, map, best_score

class Fold():
    """
    Parent Fold heeft 'eiwit' en 'algorithm' als attributen
    """
    def __init__(self, eiwit, algorithm):
        self.eiwit = eiwit
        self.algorithm = algorithm
        
class PriorityFold(Fold):
    """
    Child PriortyFold heeft 'depth' als attribuut. Elk listig pad uit listig 'paths' bestaat
    uit getupelde coordinaten die algoritme 'priority' heeft gemaakt. Elk listig karakterspad uit
    listig 'chpaths' bestaat uit tuples van een aminozuur met zijn gemapte getupelde coordinaten.
    'Score' is een methode die de vouwing van het eiwit met de meeste bonds geeft.
    """
    # def __init__(self, eiwit, algorithm, depth):
    def __init__(self, eiwit, algorithm, depth, cyclevalue):
        super().__init__(eiwit, algorithm)
        self.cyclevalue = cyclevalue
        self.depth = depth
        self.paths = priority_miro(self.depth, self.eiwit, self.cyclevalue)
        #TODO: self.priority = Priority(self.depth, self.eiwit) #nieuw
        #TODO: self.paths = self.priority.paths #nieuw
        self.chpaths = map(self.paths, self.eiwit)

    def score(self):
        #return best_score(self.chpaths)
        return best_scoorders(self.chpaths)

class CycleFold(Fold):
    """
    De 'coordinates' (en overige attributen) van het kind CycleFold komen door middels het algoritme 'cyclefold'
    die het 'eiwit' als parameter neemt en/of zijn een mapping tussen de coordinaten en het eiwit.
    """
    def __init__(self, eiwit, algorithm):
        super().__init__(eiwit, algorithm)
        self.coordinates, self.predecessors, self.directions, self.directions2 = cyclefold(self.eiwit)
        self.match, self.matcher, self.graph = mapper(self.coordinates, self.eiwit)

    def score(self):
        return scoreH(self.match, self.predecessors)

    def plot(self):
        print("\nRepresentatie:")
        for row in self.graph:
            print(row)

    def printDirections(self):
        print("\nCurrAmi: Richting")
        for tupler in range(len(self.directions2)):
            print(self.directions2[tupler][0], ",", self.directions2[tupler][1])

    def coord(self):
        return self.matcher

