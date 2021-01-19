# imports
import random
from copy import deepcopy

from Jeroen.classes.visualisation_OOP import Visualisation
from classes_hattum.grid import Grid
from classes_hattum.protein import Protein
  

class greedy_lookahead:
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

        self.perform_first_moves() 
        self.outer_loop() 

    def perform_first_moves(self):
        # append the first 2 folding moves to the list moveList
        # places the amino acids in the grid on their calculated place
        self.allMoves.append(grid.checkPossibleMoves()[0])
        self.grid.performMove(grid.checkPossibleMoves()[0], protein.code[0])
        self.allMoves.append(grid.checkPossibleMoves()[3])
        self.grid.performMove(grid.checkPossibleMoves()[3], protein.code[1])

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
        if depth == 4 or len(allMoves) == self.length:
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
                
protein = Protein("HHPHHHPH")
grid = Grid(protein.length)
algo = greedy_lookahead(protein, grid, 5)




# ## HPHPPHHPHPPHPHHPPHPH
# moveList = []
# allMoves = []


# # initialize a Protein object called protein
# protein = Protein("HHPHHHPH")
# length = protein.length

# # initialize a Grid object called grid
# grid = Grid(protein.length)

# # append all the possible folding moves to the list moveList
# allMoves.append(grid.checkPossibleMoves()[0])

# # places the amino acids in the grid on their calculated place
# grid.performMove(grid.checkPossibleMoves()[0], protein.code[0])
# allMoves.append(grid.checkPossibleMoves()[3])
# grid.performMove(grid.checkPossibleMoves()[3], protein.code[1])



# minimalScore = 0
# minimalGrid = None
# minimalPerformedMove = None
# recursionAmount = 0
# states = 0   

# def recursion_01(grid, allMoves, depth, length, firstMove, numberOfPerformedMoves):
#     """
#     recursion_01 tries to find all possible foldings of 
#     the protein by looking a set #steps (depth) ahead.
#     """

#     global minimalScore, minimalGrid, recursionAmount, minimalPerformedMove, states

#     # print the amount of recursions for convenience purposes
#     if (recursionAmount % 10000 ) == 0:
#         print(recursionAmount)
#     recursionAmount = recursionAmount + 1

#     # calculate the score of the grid when the set depth is reached or all amino acids are folded
#     if depth == 6 or len(allMoves) == protein.length:
#         S = grid.score()
#         states = states + 1
        
#         # update minimalScore & minimalGrid when a lower score is found(lower is better)
#         if S <= minimalScore and (len(grid.checkPossibleMoves()) > 0 or protein.length == 0):
#             minimalScore = S
#             minimalGrid = grid
#             minimalPerformedMove = firstMove
            
#     else:

#         # check the remaining possible moves for the current folding situation
#         moves = grid.checkPossibleMoves()

#         # TODO
#         for move in moves:
#             allMoves = allMoves[:(depth+(numberOfPerformedMoves))]
#             allMoves.append(move)
#             grid = Grid(length)
#             for allMove in allMoves:
                
#                 grid.performMove(allMove, protein.code[grid.totalMoves])
            
#             if depth == 0:
#                 recursion_01(grid, allMoves, depth+1, length, move, numberOfPerformedMoves)
#             else:
#                 recursion_01(grid, allMoves, depth+1, length, firstMove, numberOfPerformedMoves)
            

# letterPos = 2

# # perform recursion_01 as long as there are amino acids to fold 
# while protein.length > letterPos:
#     recursion_01(grid, allMoves, 0, length, None, letterPos)
#     allMoves.append(minimalPerformedMove)

#     # place the amino acid on the right place in the grid
#     grid.performMove(minimalPerformedMove, protein.code[letterPos])
#     minimalPerformedMove = None
#     minimalScore = 0
#     letterPos = letterPos + 1
#     print(letterPos)


# print(minimalGrid.score())
# minimalGrid.printGrid()
# print(states)
