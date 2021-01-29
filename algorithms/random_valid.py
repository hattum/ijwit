from copy import deepcopy
import time
import random

class Random_valid:
    def __init__(self, grid, protein, tries):
        self.protein = protein
        self.length = protein.length
        self.tries = tries
        self.grid = grid
        self.emptyGrid = deepcopy(grid)
        self.globalscore = 1
        self.allMoves = []

        self.perform()
        self.print()

    def perform(self):
        start = time.time()
        for i in range(self.tries):
            grid = deepcopy(self.emptyGrid)
            protein = deepcopy(self.protein)
            allMoves = []
            
            while protein.length > 0:
                moves = grid.checkPossibleMoves()
                if len(moves) == 0:
                    break
                
                letter = protein.pop_first_char()
                randomMove = random.choice(moves)
                allMoves.append((letter,randomMove))
                grid.performMove(randomMove,letter)
            if grid.score() < self.globalscore:
                self.allMoves = allMoves
                self.globalscore = grid.score()
                self.grid = grid
        end = time.time()
        print("The algorithme has taken: " + str(end-start) + " seconds")

    

    def print(self):
        print("The folding of the protein can be found in the new created png file")
        print("The score of the folding is: " + str(self.globalscore))

                

