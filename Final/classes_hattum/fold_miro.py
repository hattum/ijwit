import copy
import math
from queue_miro import Queue #, AminoQueue
from priorityqueue_miro import PriorityQueue
import itertools
from helpers_miro import offsets
from cyclefold import cyclefold, mapper, scoreH
from priority_miro import priority_miro, map, best_score

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
        self.match, self.graph = mapper(self.child, self.eiwit)

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

