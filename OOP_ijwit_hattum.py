# imports
import random
from copy import deepcopy

from Jeroen.classes.visualisation_OOP import Visualisation
from classes_hattum.grid import Grid
from classes_hattum.protein import Protein
  
## HPHPPHHPHPPHPHHPPHPH
moveList = []

# initialize a Protein object called protein
protein = Protein("HPHPPHHPHP")
length = protein.length

# initialize a Grid object called grid
grid = Grid(protein.length)

# append all the possible folding moves to the list moveList
moveList.append(grid.checkPossibleMoves()[0])

# places the amino acids in the grid on their calculated place
grid.performMove(grid.checkPossibleMoves()[0], protein.pop_first_char())


allMoves = []

minimalScore = 0
minimalGrid = None
minimalPerformedMove = None
   
allMoves = []
protein = Protein("HPHPPHHPHPPHPHHPPHPH")
length = protein.length
grid = Grid(length)
minimalScore = 0
minimalGrid = None
minimalPerformedMove = None
recursionAmount = 0
   
def recursion_01(grid, allMoves, depth, length, firstMove, numberOfPerformedMoves):
    """
    recursion_01 tries to find all possible foldings of 
    the protein by looking a set #steps (depth) ahead.
    """

    global minimalScore, minimalGrid, recursionAmount, minimalPerformedMove

    # print the amount of recursions for convenience purposes
    if (recursionAmount % 10000 ) == 0:
        print(recursionAmount)
    recursionAmount = recursionAmount + 1

    # calculate the score of the grid when the set depth is reached or all amino acids are folded
    if depth == 6 or len(allMoves) == protein.length:
        S = grid.score()
        
        # update minimalScore & minimalGrid when a lower score is found(lower is better)
        if S <= minimalScore and (len(grid.checkPossibleMoves()) > 0 or protein.length == 0):
            minimalScore = S
            minimalGrid = grid
            minimalPerformedMove = firstMove
            
    else:

        # check the remaining possible moves for the current folding situation
        moves = grid.checkPossibleMoves()

        # TODO
        for move in moves:
            allMoves = allMoves[:(depth+(numberOfPerformedMoves))]
            allMoves.append(move)
            grid = Grid(length)
            for allMove in allMoves:
                
                grid.performMove(allMove, protein.code[grid.totalMoves])
            
            if depth == 0:
                recursion_01(grid, allMoves, depth+1, length, move, numberOfPerformedMoves)
            else:
                recursion_01(grid, allMoves, depth+1, length, firstMove, numberOfPerformedMoves)
            

letterPos = 0

# perform recursion_01 as long as there are amino acids to fold 
while protein.length > letterPos:
    recursion_01(grid, allMoves, 0, length, None, letterPos)
    allMoves.append(minimalPerformedMove)

    # place the amino acid on the right place in the grid
    grid.performMove(minimalPerformedMove, protein.code[letterPos])
    minimalPerformedMove = None
    minimalScore = 0
    letterPos = letterPos + 1
    print(letterPos)

print(grid.score())
grid.printGrid()
# print(minimalScore)
# grid.printGrid()