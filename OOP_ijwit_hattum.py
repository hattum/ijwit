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
   
def recursion_01(grid, allMoves, depth, length, firstMove, numberOfPerformedMoves):
    """This is a recursive function
    to find all possible folds"""

    global minimalScore, minimalGrid
    

    if depth == 6 or protein.length == 0:
        S = grid.score()
        
        
        if S <= minimalScore and (len(grid.checkPossibleMoves()) > 0 or protein.length == 0):
            
            minimalScore = S
            minimalGrid = grid
            minimalPerformedMove = firstMove
            
    else:
        moves = grid.checkPossibleMoves()
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
while protein.length > letterPos:
    recursion_01(grid, allMoves, 0, length, None, letterPos)
    allMoves.append(minimalPerformedMove)
    grid.performMove(minimalPerformedMove, protein.code[letterPos])
    minimalPerformedMove = None
    minimalScore = 0
    letterPos = letterPos +1
    print(letterPos)

print(grid.score())
grid.printGrid()
# print(minimalScore)
# grid.printGrid()