# imports
import random
from copy import deepcopy

from Jeroen.classes.visualisation_OOP import Visualisation
from classes_hattum.grid import Grid
from classes_hattum.protein import Protein
  




## HPHPPHHPHPPHPHHPPHPH
moveList = []
allMoves = []


# initialize a Protein object called protein
protein = Protein("HHPHHHPHPHHHPH")
length = protein.length

# initialize a Grid object called grid
grid = Grid(protein.length)

# append all the possible folding moves to the list moveList
allMoves.append(grid.checkPossibleMoves()[0])

# places the amino acids in the grid on their calculated place
grid.performMove(grid.checkPossibleMoves()[0], protein.code[0])
allMoves.append(grid.checkPossibleMoves()[3])
grid.performMove(grid.checkPossibleMoves()[3], protein.code[1])
grid.printGrid()



minimalScore = 0
minimalGrid = None
minimalPerformedMove = None
recursionAmount = 0
states = 0   

def recursion_01(grid, allMoves, depth, length, firstMove, numberOfPerformedMoves):
    """This is a recursive function
    to find all possible folds"""

    global minimalScore, minimalGrid, recursionAmount, minimalPerformedMove, states

    if (recursionAmount % 10000 )== 0:
        print(recursionAmount)
    recursionAmount = recursionAmount+1

    if depth == 7 or len(allMoves) == protein.length:
        
        
        S = grid.score()
        states = states + 1
        
        
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
            

letterPos = 2
while protein.length > letterPos:
    recursion_01(grid, allMoves, 0, length, None, letterPos)
    allMoves.append(minimalPerformedMove)
    grid.performMove(minimalPerformedMove, protein.code[letterPos])
    minimalPerformedMove = None
    minimalScore = 0
    letterPos = letterPos +1
    print(letterPos)


print(minimalGrid.score())
minimalGrid.printGrid()
print(states)
