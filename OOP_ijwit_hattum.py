import random
from copy import deepcopy

from Jeroen.classes.visualisation_OOP import Visualisation

from classes_hattum.protein import Protein
from classes_hattum.grid import Grid

# HPHPPHHPHPPHPHHPPHPH
allMoves = []
protein = Protein("HPHPPHHPHPPHPHHPPHPH")
length = protein.length
grid = Grid(length)
minimalScore = 0
minimalGrid = None
minimalPerformedMove = None
recursionAmount = 0
   
def recursion_01(grid, allMoves, depth, length, firstMove, numberOfPerformedMoves):
    """This is a recursive function
    to find all possible folds"""

    global minimalScore, minimalGrid, recursionAmount, minimalPerformedMove

    if (recursionAmount % 10000 )== 0:
        print(recursionAmount)
    recursionAmount = recursionAmount+1

    if depth == 10 or len(allMoves) == protein.length:
        
        
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