# imports
from copy import deepcopy
  

class Greedy_lookahead:
    def __init__(self, protein, grid, lookahead):
        self.protein = protein
        self.length = protein.length
        self.grid = grid
        self.emptyGrid = deepcopy(grid)
        self.allMoves = []
        self.minimalScore = 0
        self.minimalGrid = None
        self.minimalPerformedMove = None
        self.recursionAmount = 0
        self.states = 0 
        self.lookahead = lookahead

        self.perform_first_moves() 
        self.outer_loop() 

    def perform_first_moves(self):
        # append the first 2 folding moves to the list moveList
        # places the amino acids in the grid on their calculated place
        self.allMoves.append(self.grid.checkPossibleMoves()[0])
        self.grid.performMove(self.grid.checkPossibleMoves()[0], self.protein.code[0])
        self.allMoves.append(self.grid.checkPossibleMoves()[3])
        self.grid.performMove(self.grid.checkPossibleMoves()[3], self.protein.code[1])

    def outer_loop(self):
        # perform recursion_01 as long as there are amino acids to fold 
        while self.protein.length > self.grid.totalMoves:
            grid = deepcopy(self.grid)
            self.recursion_01(grid, self.allMoves, 0, self.length, None, self.grid.totalMoves)
            self.allMoves.append(self.minimalPerformedMove)

            # place the amino acid on the right place in the grid
            self.grid.performMove(self.minimalPerformedMove, self.protein.code[self.grid.totalMoves])
            self.minimalPerformedMove = None
            self.minimalScore = 0
            print(self.grid.totalMoves)

        print(self.minimalGrid.score())
        self.grid.printGrid()
        print("total states = " + str(self.states))
    
    
    def recursion_01(self, grid, allMoves, depth, length, firstMove, numberOfPerformedMoves):
        """
        recursion_01 tries to find all possible foldings of 
        the protein by looking a set #steps (depth) ahead.
        """
        


        # print the amount of recursions for convenience purposes
        if (self.recursionAmount % 10000 ) == 0:
            print(self.recursionAmount)
        self.recursionAmount = self.recursionAmount + 1

        # calculate the score of the grid when the set depth is reached or all amino acids are folded
        if depth == self.lookahead or len(allMoves) == self.length:
            S = grid.score()
            self.states = self.states + 1
            
            # update minimalScore & minimalGrid when a lower score is found(lower is better)
            if S <= self.minimalScore and (len(grid.checkPossibleMoves()) > 0 or self.protein.length == self.grid.totalMoves):
                self.minimalScore = S
                self.minimalGrid = grid
                self.minimalPerformedMove = firstMove
                
        else:

            # check the remaining possible moves for the current folding situation
            moves = grid.checkPossibleMoves()

            # TODO
            for move in moves:
                allMoves = allMoves[:(depth+(numberOfPerformedMoves))]
                allMoves.append(move)
               
                grid.clearGrid()

            
                for allMove in allMoves:
                    grid.performMove(allMove, self.protein.code[grid.totalMoves])
    
                if depth == 0:
                    self.recursion_01(grid, allMoves, depth+1, length, move, numberOfPerformedMoves)
                else:
                    self.recursion_01(grid, allMoves, depth+1, length, firstMove, numberOfPerformedMoves)
                
