import copy
from classes.priorityqueue_miro import PriorityQueue
from assets.helpers_miro import offsets

class PriorityFold():
    """
    Initialize class PriorityFold with selected eiwit from the UI.
    Depth is either get from the UI or otherwise depth equals to the length of the proteine
    The other attributes you get for free
    """

    def __init__(self, eiwit, depth, cyclevalue, heuristic):
        self.eiwit = eiwit
        self.depth = depth
        self.cyclevalue = cyclevalue
        self.heuristic = heuristic
        self.hpotentials, self.cpotentials = potentials(self.eiwit, self.depth) #nieuw
        self.pq = PriorityQueue()
        self.pq.put([(0,0),(-1,0)], 0)
        self.maxscore = 0
        self.paths = []
        
    def folder(self, state, direction):
        """
        make a child from the state of the unfolding proteine with the given direction, 
        compare the created priority of the child to the maxscore within the family,
        put the child back into the family when it has potential to transcend the maxscore
        """
        child = copy.deepcopy(state)
        neighbour_pos = (state[-1][0] + offsets[direction][0], 
                                state[-1][1] + offsets[direction][1])
        if neighbour_pos not in child and child not in self.paths:
            child += [neighbour_pos]
            aminoschecked = self.eiwit[:(len(state)+ 1)]
            childmatch = mapper(child, aminoschecked)
            h_value = get_heuristic(self.eiwit, state, self.hpotentials, self.cpotentials, self.depth, self.cyclevalue, self.heuristic)
            score = scoreH(childmatch)
            priority = score + h_value
            if priority <= self.maxscore:
                self.pq.put(child, priority)
            print("Pending maxscore is:", self.maxscore)
            if score < self.maxscore:
                self.maxscore = score
            if len(child) == self.depth:
                self.paths.append(child)

    def run(self):
        """
        keep on making children and accepting them in case they are strong,
        check symmetry in order to reduce the statespace
        """
        while not self.pq.is_empty():
            state = self.pq.get()
            if len(state) < self.depth:
                if is_symm(state):
                    for direction in ["2", "1"]:
                        self.folder(state, direction)
                else:
                    for direction in ["2", "1", "-2", "-1"]:
                        self.folder(state, direction)
        return self.paths

    def score(self):
        """
        make match among all possible paths and the proteine and return winner, best_score
        """
        pathsmatch = map(self.paths, self.eiwit)
        return best_score(pathsmatch)

def is_symm(state):
    """
    check if the current state is vertically aligned
    """
    for i in range(1, len(state)):
        if state[i][1] != state[i-1][1]:
            return False
    return True


def mapper(coords, eiwit):
    """
    map the assigned coordinates with the aminos
    """
    coordsmatch = []
    for element in zip(coords, eiwit):
        pos = element[0]
        amino = element[1]
        coordsmatch.append((amino, pos))
    return coordsmatch

def map(paths, eiwit):
    """
    map the assigned coordinates with the aminos of all possible paths
    """
    pathsmatch = []
    for child in paths:
        childmatch = mapper(child, eiwit)
        pathsmatch.append(childmatch)
    return pathsmatch


def scoreH(coordsmatch):
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


def best_score(paths):
    """
    returns a single winner and related best_score out of all possible paths
    """
    bestscore = 0
    for path in paths:
        score = scoreH(path)
        if score <= bestscore:
            winner = path
            bestscore = score
    try:
        return winner, bestscore
    except:
        raise Exception("score was not in range")


def potentials(eiwit, depth):
    """
    make registers of potential scores of bonds
    """
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
    """
    calculate the number of H's and C's and divide by the set depth
    """
    count = 0
    for i in range(0, depth):
        if eiwit[i] == "H" or eiwit[i] == "C":
            count += 1
    return count/depth


def get_heuristic(eiwit, child, hpotentials, cpotentials, depth, cyclevalue, heuristic):
    """
    returns the heuristic value related to the unfolding of the proteine so far.
    the heuristic value refers to the potential scores of upcoming bonds if unfolding proceeds
    """
    if heuristic == "admissable":
        return -((hpotentials[len(child) - 1]) * 2) - ((cpotentials[len(child) - 1]) * 5) -1
    if heuristic == "regular":
        return -((hpotentials[len(child) - 1]) * ((depth + 1)/depth)) - ((cpotentials[len(child) - 1]) * ((depth + 1)/depth))
    if heuristic == "cyclebased":
        return -((hpotentials[len(child) - 1]) * (-cyclevalue/depth)) - ((cpotentials[len(child) - 1]) * (-cyclevalue/depth))
    if heuristic == "cyclereducedbyfactor":
        number = factor(eiwit, depth)
        return -((hpotentials[len(child) - 1]) * (-cyclevalue/depth)) - ((cpotentials[len(child) - 1]) * (-cyclevalue/depth)) * number

