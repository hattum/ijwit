import copy
import math
import itertools
from classes_hattum.queue_miro import Queue
from classes_hattum.priorityqueue_miro import PriorityQueue
from assets.helpers_miro import offsets
from algorithms_hattum.cyclefold import cyclefold, mapper, scoreH
from algorithms_hattum.priority_miro import priority_miro, map, best_score

class Fold():
    def __init__(self, eiwit, algorithm):
        self.eiwit = eiwit
        self.algorithm = algorithm
        self.paths = []
        self.graph = [["   " for i in range(len(self.eiwit))] for i in range(len(self.eiwit))]

class PriorityFold(Fold):
    def __init__(self, eiwit, algorithm, depth):
        super().__init__(eiwit, algorithm)
        self.depth = depth
        self.paths = priority_miro(self.depth, self.eiwit)
        self.chpaths = map(self.paths, self.eiwit)

    def score(self):
        return best_score(self.chpaths)

class CycleFold(Fold):
    def __init__(self, eiwit, algorithm):
        super().__init__(eiwit, algorithm)
        self.child, self.predecessors, self.directions, self.directions2 = cyclefold(self.eiwit)
        self.match, self.matcher, self.graph = mapper(self.child, self.eiwit)

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

    # def coord(self):
    #     coordinates = []
    #     print("\nPositie: Amino")
    #     for amino in self.match:
    #         print(amino, ":" , self.match[amino])
    #     for key, value in self.match.items():
    #         coordinates += [(value, key)]
    #     return coordinates

    def coord(self):
        return self.matcher

